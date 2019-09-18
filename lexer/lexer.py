from token import Tokens
from token import Token

# 暂时的输入
def scanner():
    i = input('Please enter a regular expression: ')
    return i


class Lexer(object):
    def __init__(self, input):
        self.input = input
        self.pos = 0
        self.isescape = False
        self.current_token = None

    def advance(self):
        pos = self.pos
        input = self.input
        if pos > len(input) - 1:
            return Token.EOS

        print('**debug ', pos)
        text = input[pos]
        if text == '\\':
            self.isescape = not self.isescape
            self.pos = self.pos + 1
            self.current_token =  self.handle_escape()
        else:
            self.current_token = self.handle_semantic_l(text)

        return self.current_token

    def handle_escape(self):
        expr = self.input.lower()
        pos = self.pos
        ev = {
            '\0' : '\\',
            'b' : '\b',
            'f' : '\f',
            'n' : '\n',
            's' : ' ',
            't' : '\t',
            'e' : '\033',
        }
        rval = ev.get(expr[pos])
        if rval is None:
            if expr[pos] == '^':
                rval = self.handle_tip()
            elif expr[pos] == 'O':
                rval = self.handle_oct()
            elif expr[pos] == 'X':
                rval = self.handle_hex()   
            else:
                rval = Token.L
        self.pos = self.pos + 1        
        return rval

    def handle_semantic_l(self, text):
        self.pos = self.pos + 1
        return Tokens.get(text, Token.L)

    def handle_tip(self):
        self.pos = self.pos + 1
        return self.input[self.pos] - '@'

    def handle_oct(self):
        return 1

    def handle_hex(self):            
        return 1

i = scanner()
lexer = Lexer(i)
for i in range(len(i)):
    lexer.advance()
    print(lexer.current_token)