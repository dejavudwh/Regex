from parse.parse import match
from parse.parse_dfa import dfa_match 
from nfa.construction import pattern
from parse.parse_dfa import get_jump_table


class Regex(object):
    def __init__(self, input_string, pattern_string, mode=1, minimize=True):
        self.input_string = input_string
        self.pattern_string = pattern_string
        self.mode = mode
        self.minimize = minimize

    def match(self):
        pattern_string = self.pattern_string
        input_string = self.input_string
        if self.mode == 2:
            jump_table = get_jump_table(pattern_string, self.minimize)
            return dfa_match(input_string, jump_table, self.minimize)
        else:
            nfa_machine = pattern(pattern_string)
            return match(input_string, nfa_machine)            

    def replace():
        pass

    def search():
        pass