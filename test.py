from nfa.construction import (
    nfa_dot_char,
    nfa_single_char,
    nfa_set_char,
)
from nfa.nfa import debugNfa
from nfa.nfa import NfaPair


nfa_pair = NfaPair()
# start = Nfa() # 0
# node1 = start.next_1 = Nfa() # 1
# node2 = start.next_2 = Nfa() # 2
# node1.next_1 = Nfa() # 3
# node1.next_1 = Nfa() # 4
# node2.next_2 = Nfa() # 5
nfa_dot_char(nfa_pair)
nfa_single_char(nfa_pair)
nfa_set_char(nfa_pair)

# debugNfa(nfa_pair.start_node)

