from lex.token import Token
from lex.lexer import scanner
from lex.lexer import Lexer
from nfa.nfa import Nfa
from nfa.nfa import EPSILON
from nfa.nfa import CCL
from nfa.nfa import EMPTY


s = scanner()
lexer = Lexer(s)
lexer.advance()


# 对 . a (单个字符) [] 进行匹配
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