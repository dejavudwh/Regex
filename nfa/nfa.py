class Nfa(object):
    STATUS_NUM = 0
    def __init__(self):
        self.edge = None
        self.next_1 = None
        self.next_2 = None
        self.visited = False
        self.set_status_num()

    def set_status_num(self):
        self.status_num = Nfa.STATUS_NUM
        Nfa.STATUS_NUM = Nfa.STATUS_NUM + 1

class NfaPair(object):
    def __init__(self):
        self.start_node = None
        self.end_node = None

def debugNfa(start_node):
    if start_node is None:
        return None
    print('status num: ', start_node.status_num)
    next_1_node = start_node.next_1 is not None
    next_2_node = start_node.next_2 is not None
    if next_1_node:
        print('next 1: ', start_node.next_1.status_num)
    if next_2_node:
        print('next 2: ', start_node.next_2.status_num) 

    debugNfa(start_node.next_1)
    debugNfa(start_node.next_2)

start = Nfa() # 0
node1 = start.next_1 = Nfa() # 1
node2 = start.next_2 = Nfa() # 2
node1.next_1 = Nfa() # 3
node2.next_2 = Nfa() # 4

debugNfa(start)