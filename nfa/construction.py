from lex.token import Token
from lex.lexer import Lexer
from nfa.nfa import (
    Nfa,
    NfaPair,
    log_nfa,
)
from nfa.nfa import (
    EPSILON,
    CCL,
    EMPTY,
    ASCII_COUNT,
)


lexer = None


def pattern(pattern_string):
    global lexer
    lexer = Lexer(pattern_string)
    lexer.advance()
    nfa_pair = NfaPair()
    group(nfa_pair)
    # log_nfa(nfa_pair.start_node)

    return nfa_pair.start_node


"""
group ::= ("(" expr ")")*
expr ::= factor_conn ("|" factor_conn)*
factor_conn ::= factor | factor factor*
factor ::= (term | term ("*" | "+" | "?"))*
term ::= char | "[" char "-" char "]" | .
"""


# 对 . a (单个字符) [] 进行匹配
def term(pair_out):
    if lexer.match(Token.L):
        nfa_single_char(pair_out)
    elif lexer.match(Token.ANY):
        nfa_dot_char(pair_out)
    elif lexer.match(Token.CCL_START):
        nfa_set_nega_char(pair_out)


# 匹配单个字符
def nfa_single_char(pair_out):
    if not lexer.match(Token.L):
        return False

    start = pair_out.start_node = Nfa()
    pair_out.end_node = pair_out.start_node.next_1 = Nfa()
    start.edge = lexer.lexeme
    lexer.advance()
    return True


# . 匹配任意单个字符
def nfa_dot_char(pair_out):
    if not lexer.match(Token.ANY):
        return False

    start = pair_out.start_node = Nfa()
    pair_out.end_node = pair_out.start_node.next_1 = Nfa()
    start.edge = CCL
    start.set_input_set()

    lexer.advance()
    return False


# [] 匹配字符集
def nfa_set_char(pair_out):
    if not lexer.match(Token.CCL_START):
        return False

    start = pair_out.start_node = Nfa()
    pair_out.end_node = pair_out.start_node.next_1 = Nfa()
    start.edge = CCL
    start.input_set = set()
    dodash(start.input_set)

    lexer.advance()
    return True


def nfa_set_nega_char(pair_out):
    if not lexer.match(Token.CCL_START):
        return False
    
    neagtion = False
    lexer.advance()
    if lexer.match(Token.AT_BOL):
        neagtion = True
    
    start = pair_out.start_node = Nfa()
    start.next_1 = pair_out.end_node = Nfa()
    start.edge = CCL
    dodash(start.input_set)

    if neagtion:
        char_set_inversion(start.input_set)

    lexer.advance()
    return True


def char_set_inversion(input_set):
    for i in range(ASCII_COUNT):
        c = chr(i)
        if c not in input_set:
            input_set.add(c)


def dodash(input_set):
    first = ''
    while not lexer.match(Token.CCL_END):
        if not lexer.match(Token.DASH):
            first = lexer.lexeme
            input_set.add(first)
        else:
            lexer.advance()
            for c in range(ord(first), ord(lexer.lexeme) + 1):
                input_set.add(chr(c))
        lexer.advance()


# factor connect
def factor_conn(pair_out):
    if is_conn(lexer.current_token):
        factor(pair_out)
    
    while is_conn(lexer.current_token):
        pair = NfaPair()
        factor(pair)
        pair_out.end_node.next_1 = pair.start_node
        pair_out.end_node = pair.end_node

    return True


def is_conn(token):
    nc = [
        Token.OPEN_PAREN,
        Token.CLOSE_PAREN,
        Token.AT_EOL,
        Token.EOS,
        Token.CLOSURE,
        Token.PLUS_CLOSE,
        Token.CCL_END,
        Token.AT_BOL,
        Token.OR,
    ]
    return token not in nc


# factor * + ? closure
def factor(pair_out):
    term(pair_out)
    if lexer.match(Token.CLOSURE):
        nfa_star_closure(pair_out)
    elif lexer.match(Token.PLUS_CLOSE):
        nfa_plus_closure(pair_out)
    elif lexer.match(Token.OPTIONAL):
        nfa_option_closure(pair_out)


# * 闭包操作
def nfa_star_closure(pair_out):
    if not lexer.match(Token.CLOSURE):
        return False
    start = Nfa()
    end = Nfa()
    start.next_1 = pair_out.start_node
    start.next_2 = end

    pair_out.end_node.next_1 = pair_out.start_node
    pair_out.end_node.next_2 = end

    pair_out.start_node = start
    pair_out.end_node = end

    lexer.advance()
    return True


# + 正闭包
def nfa_plus_closure(pair_out):
    if not lexer.match(Token.PLUS_CLOSE):
        return False
    start = Nfa()
    end = Nfa()
    start.next_1 = pair_out.start_node

    pair_out.end_node.next_1 = pair_out.start_node
    pair_out.end_node.next_2 = end

    pair_out.start_node = start
    pair_out.end_node = end

    lexer.advance()
    return True


# ?
def nfa_option_closure(pair_out):
    if not lexer.match(Token.OPTIONAL):
        return False
    start = Nfa()
    end = Nfa()

    start.next_1 = pair_out.start_node
    start.next_2 = end
    pair_out.end_node.next_1 = end

    pair_out.start_node = start
    pair_out.end_node = end

    lexer.advance()
    return True


def expr(pair_out):
    factor_conn(pair_out)
    pair = NfaPair()

    while lexer.match(Token.OR):
        lexer.advance()
        factor_conn(pair)
        start = Nfa()
        start.next_1 = pair.start_node
        start.next_2 = pair_out.start_node
        pair_out.start_node = start

        end = Nfa()
        pair.end_node.next_1 = end
        pair_out.end_node.next_2 = end
        pair_out.end_node = end

    return True


def group(pair_out):
    if lexer.match(Token.OPEN_PAREN):
        lexer.advance()
        expr(pair_out)
        if lexer.match(Token.CLOSE_PAREN):
            lexer.advance()
    elif lexer.match(Token.EOS):
        return False
    else: 
        expr(pair_out)

    while True:
        pair = NfaPair()
        if lexer.match(Token.OPEN_PAREN):
            lexer.advance()
            expr(pair)
            pair_out.end_node.next_1 = pair.start_node
            pair_out.end_node = pair.end_node
            if lexer.match(Token.CLOSE_PAREN):
                lexer.advance()
        elif lexer.match(Token.EOS):
            return False
        else: 
            expr(pair)
            pair_out.end_node.next_1 = pair.start_node
            pair_out.end_node = pair.end_node

    
    