from parse.parse import match


class Regex(object):
    def __init__(self, input_string, pattern_string):
        self.input_string = input_string
        self.pattern_string = pattern_string

    def match(self):
        return match(self.input_string, self.pattern_string)

    def replace():
        pass

    def search():
        pass