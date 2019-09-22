from dfa.construction import convert_to_dfa
from nfa.construction import pattern


def get_jump_table(pattern_string):
    nfa_start_node = pattern(pattern_string)
    jump_table = convert_to_dfa(nfa_start_node)

    return jump_table


def dfa_match(input_string, pattern_string):
    jump_table = get_jump_table(pattern_string)

    cur_status = 0 
    for i, c in enumerate(input_string):
        print("now match ******** ", c)
        jump_dict = jump_table[cur_status]
        if jump_dict:
            js = jump_dict.get(c)
            if js is None:
                return False
            else:
                cur_status = js
        print(i, jump_dict.get('accepted'), cur_status, js)
        if i == len(input_string) - 1 and jump_dict.get('accepted'):
            print('match **************** ', i, cur_status, jump_dict, jump_table)
            return True

    return jump_table[cur_status].get('accepted') is not None