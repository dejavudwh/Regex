from dfa.construction import dfa_list
from dfa.dfa_group import DfaGroup
from parse_dfa import get_jump_table
from nfa.nfa import ASCII_COUNT


group_list = []
jump_table = get_jump_table()


def minimize_dfa():
    group_a, group_na = partition_accepted()
    group_list.append(group_a)
    group_list.append(group_na)
    pass


def partition_accepted():
    group_na = DfaGroup()
    group_a = DfaGroup()
    for dfa in dfa_list:
        if dfa.accepted:
            group_a.append(dfa)
        else:
            group_na.append(dfa)

    return group_a, group_na


def partition_on_num():
    pass


def partition_on_char():
    for group in group_list:
        dfa_index = 1
        first_dfa = group.get(0)
        next_dfa = group.get(dfa_index)

        while next_dfa is not None:
            for i in range(ASCII_COUNT):
                ch = chr(i)
                if not str.isdigit(ch) and partition(group, first_dfa, next_dfa, ch):


def partition(group, first, next, ch):
    goto_first = jump_table[first.status_num].get(ch)
    goto_next = jump_table[next.status_num].get(ch)

    if dfa_in_group(goto_first) != dfa_in_group(goto_next):
        new_group = DfaGroup()
        group_list.append(new_group)
        group.remove(goto_next)
        new_group.add(goto_next)
        return True
        
    return False


def dfa_in_group(status_num):
    for group in group_list:
        for dfa in group:
            if dfa.status_num == status_num:
                return group
    return None

