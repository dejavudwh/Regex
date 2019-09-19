class Text(object):
    status_num = 0
    def __init__(self):
        self.f = None

Text.status_num = 2
print(Text.status_num)
Text.status_num = 3
print(Text.status_num)