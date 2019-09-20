from nfa.construction import (
    expr,
)
from nfa.nfa import NfaPair
from nfa.nfa import (
    log_nfa,
)
from lex.lexer import Lexer


nfa_pair = NfaPair()
# start = Nfa() # 0
# node1 = start.next_1 = Nfa() # 1
# node2 = start.next_2 = Nfa() # 2
# node1.next_1 = Nfa() # 3
# node1.next_1 = Nfa() # 4
# node2.next_2 = Nfa() # 5
# term(nfa_pair)
# nfa_star_closure(nfa_pair)
# term(nfa_pair)
# nfa_option_closure(nfa_pair)
# debugNfa(nfa_pair.start_node)
# factor(nfa_pair)
# factor_conn(nfa_pair)
expr(nfa_pair)
log_nfa(nfa_pair.start_node)