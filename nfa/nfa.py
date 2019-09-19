# 对应的节点有两个出去的ε边
EPSILON = -1
# 边对应的是字符集
CCL = -2
# 一条ε边
EMPTY = -3
ASCII_COUNT = 127


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

    def set_input_set(self):
        self.input_set = set()
        for i in range(ASCII_COUNT):
            self.input_set.add(chr(i))


class NfaPair(object):
    def __init__(self):
        self.start_node = None
        self.end_node = None

def debugNfa(start_node):
    if start_node is None:
        return None
    print('status num: ', start_node.status_num)
    if start_node.next_1 is not None:
        print('next 1: ', start_node.next_1.status_num)
    if start_node.next_2 is not None:
        print('next 2: ', start_node.next_2.status_num) 

    debugNfa(start_node.next_1)
    debugNfa(start_node.next_2)

# start = Nfa() # 0
# node1 = start.next_1 = Nfa() # 1
# node2 = start.next_2 = Nfa() # 2
# node1.next_1 = Nfa() # 3
# node2.next_2 = Nfa() # 4

# debugNfa(start)

# start.set_input_set()
# print(start.input_set)