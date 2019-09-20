from lex.token import Token
from lex.lexer import scanner
from lex.lexer import Lexer
from nfa.nfa import (
    Nfa,
    NfaPair,
)
from nfa.nfa import EPSILON
from nfa.nfa import CCL
from nfa.nfa import EMPTY


s = scanner()
lexer = Lexer(s)
lexer.advance()


# 对 . a (单个字符) [] 进行匹配
# term -> a | [] | .
def term(pair_out):
    if lexer.match(Token.L):
        nfa_single_char(pair_out)
    elif lexer.match(Token.ANY):
        nfa_dot_char(pair_out)
    elif lexer.match(Token.CCL_START):
        nfa_set_char(pair_out)


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


def dodash(input_set):
    first = ''
    lexer.advance()
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
# factor -> factor factor
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
        Token.CLOSE_PAREN,
        Token.AT_EOL,
        Token.EOS,
        Token.CLOSURE,
        Token.PLUS_CLOSE,
        Token.CCL_END,
        Token.AT_BOL,
    ]
    print(lexer.current_token, token not in nc)
    return token not in nc


# factor * + ? closure
# factor -> term* | term+ | term?
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
    print(lexer.current_token, '****')
    lexer.advance()
    print(lexer.current_token, '****')
    return True
