from parse.parse import match
from parse.parse_dfa import dfa_match 


class Regex(object):
    def __init__(self, input_string, pattern_string, mode=1, minimize=True):
        self.input_string = input_string
        self.pattern_string = pattern_string
        self.mode = mode
        self.minimize = minimize

    def match(self):
        if self.mode == 2:
            return dfa_match(self.input_string, self.pattern_string, self.minimize)
        return match(self.input_string, self.pattern_string)            

    def replace():
        pass

    def search():
        pass