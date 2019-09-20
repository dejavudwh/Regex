from nfa.construction import (
    term,
    nfa_star_closure,
    nfa_plus_closure,
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
term(nfa_pair)
nfa_star_closure(nfa_pair)
term(nfa_pair)
nfa_plus_closure(nfa_pair)
# debugNfa(nfa_pair.start_node)

