
from lex.token import Token
from lex.lexer import scanner
from lex.lexer import Lexer
from nfa import Nfa
from nfa import EPSILON
from nfa import CCL
from nfa import EMPTY

s = scanner()
lexer = Lexer(s)

# 匹配单个字符
def nfa_single_char(pair_out):
    if not lexer.match(Token.L):
        return False

    start = pair_out.start_node = Nfa() 
    pair_out = pair_out.start_node.next_1 = Nfa()   
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
    dodash(start.input_set)

    lexer.advance()
    
    return True


def dodash(input_set):
    first = ''
    while not lexer.match(Token.CCL_END):
        if not lexer.match(Token.DASH):
            first = lexer.lexeme
        else:
            lexer.advance()
            for c in range(ord(first), ord(lexer.lexeme) + 1):
                input_set.add(chr(c))
        lexer.advance()        

# i = set()
# dodash(i)
# print(i)