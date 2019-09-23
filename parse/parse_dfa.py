from dfa.construction import convert_to_dfa
from nfa.construction import pattern
from dfa.minimize_dfa import minimize_dfa
from dfa.minimize_dfa import dfa_in_group


def get_jump_table(pattern_string, minimize=True):
    nfa_start_node = pattern(pattern_string)
    global jump_table
    jump_table = convert_to_dfa(nfa_start_node)

    if minimize:
        return minimize_dfa(jump_table)
    return jump_table


def dfa_match(input_string, pattern_string, minimize=True):
    jump_table = get_jump_table(pattern_string, minimize)

    if minimize:
        cur_status = dfa_in_group(0).group_num
    else:
        cur_status = 0 
    for i, c in enumerate(input_string):
        jump_dict = jump_table[cur_status]
        if jump_dict:
            js = jump_dict.get(c)
            if js is None:
                return False
            else:
                cur_status = js
        if i == len(input_string) - 1 and jump_dict.get('accepted'):
            return True

    return jump_table[cur_status].get('accepted') is not None