from lexer.lexer import Lexer
from lexer.lexer import scanner
from lexer.token import Token
from nfa import Nfa

s = scanner()
lexer = Lexer(s)

def nfa_single_char(pair_out):
    if not lexer.match(Token.L):
        return False

    start = pair_out.start_node = Nfa() 
    pair_out = pair_out.start_node.next_1 = Nfa()   
    start.edge = lexer.lexeme
    lexer.advance()
    return True