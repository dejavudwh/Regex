from utils import log

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
        self.edge = EPSILON
        self.next_1 = None
        self.next_2 = None
        self.visited = False
        self.input_set = set()
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


def log_nfa(start_node):
    log('NFA: ******** ')
    next_1 = start_node.next_1 is not None
    next_2 = start_node.next_2 is not None
    if next_1:
        log('from: ', start_node.status_num)
        log('to: ', start_node.next_1.status_num)
        log('in: ', start_node.edge)

    if next_2:
        log('from: ', start_node.status_num)
        log('to: ', start_node.next_2.status_num)
        log('in: ', start_node.edge)

    if not next_1 and not next_2:
        log('accept: ', start_node.status_num)

    start_node.visited = True
    if hasattr(start_node, 'input_set'):
        log('input set: ', start_node.input_set)

    if start_node.next_1 is not None and not start_node.next_1.visited:
        log_nfa(start_node.next_1)
    if start_node.next_2 is not None and not start_node.next_2.visited:
        log_nfa(start_node.next_2)
