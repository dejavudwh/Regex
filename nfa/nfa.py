class Nfa(object):
    def __init__(self):
        self.edge = None
        self.next_1 = None
        self.next_2 = None
        self.statu_num = -1
        self.visited = False


class NfaPair(object):
    def __init__(self):
        self.start_node = None
        self.end_node = None
