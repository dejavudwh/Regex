from parse.parse import (
    closure,
    move,
)
from dfa.dfa import (
    Dfa,
    MAX_DFA_STATUS_NUM,
)
from nfa.nfa import ASCII_COUNT
from utils import list_dict


dfa_list = []


def convert_to_dfa(nfa_start_node):
    jump_table = list_dict(MAX_DFA_STATUS_NUM)
    ns = [nfa_start_node]
    n_closure = closure(ns)
    dfa = Dfa.nfas_to_dfa(n_closure)
    dfa_list.append(dfa)

    dfa_index = 0
    while dfa_index < len(dfa_list):
        dfa = dfa_list[dfa_index]
        for i in range(ASCII_COUNT):
            c = chr(i)
            nfa_move = move(dfa.nfa_sets, c)
            if nfa_move is not None:
                nfa_closure = closure(nfa_move)
                if nfa_closure is None:
                    continue
                new_dfa = convert_completed(dfa_list, nfa_closure)
                if new_dfa is None:
                    new_dfa = Dfa.nfas_to_dfa(nfa_closure)
                    dfa_list.append(new_dfa)
                next_state = new_dfa.status_num
            jump_table[dfa.status_num][c] = next_state
            if new_dfa.accepted:
                jump_table[new_dfa.status_num]['accepted'] = True
        dfa_index = dfa_index + 1
    
    return jump_table
    

def convert_completed(dfa_list, closure):
    for dfa in dfa_list:
        if dfa.nfa_sets == closure:
            return dfa

    return None


def log_dfa(dfa_list):
    for dfa in dfa_list:
        print('dfa num: ', dfa.status_num, dfa.accepted)
        for nfa in dfa.nfa_sets:
            print('     nfa sets: ', nfa.status_num)