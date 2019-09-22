from dfa.construction import dfa_list
from dfa.dfa_group import DfaGroup
from nfa.nfa import ASCII_COUNT
from utils import list_dict


group_list = []
on_partition = True


def minimize_dfa(jump_table):
    partition_accepted()

    global on_partition
    while on_partition:
        on_partition = False
        partition_on_num(jump_table)
        partition_on_char(jump_table)

    return create_mindfa_table(jump_table)


def partition_accepted():
    group_na = []
    group_a = []
    for dfa in dfa_list:
        if dfa.accepted:
            group_a.append(dfa)
        else:
            group_na.append(dfa)
    
    if len(group_a) > 0:
        append_group(group_a)
    if len(group_na) > 0:
        append_group(group_na)


def append_group(group_a):
    group = DfaGroup()
    group.group = group_a
    group_list.append(group)


def partition_on_num(jump_table):
    for group in group_list:
        dfa_index = 1
        first_dfa = group.get(0)
        next_dfa = group.get(dfa_index)

        while next_dfa is not None:
            for i in range(10):
                ch = str(i)
                if partition(jump_table, group, first_dfa, next_dfa, ch):
                    global on_partition
                    on_partition = True
                    break
            dfa_index = dfa_index + 1
            next_dfa = group.get(dfa_index)


def partition_on_char(jump_table):
    for group in group_list:
        dfa_index = 1
        first_dfa = group.get(0)
        next_dfa = group.get(dfa_index)

        while next_dfa is not None:
            for i in range(ASCII_COUNT):
                ch = chr(i)
                if not str.isdigit(ch) and partition(jump_table, group, first_dfa, next_dfa, ch):
                    global on_partition
                    on_partition = True
                    break
            dfa_index = dfa_index + 1
            next_dfa = group.get(dfa_index)


def partition(jump_table, group, first, next, ch):
    goto_first = jump_table[first.status_num].get(ch)
    goto_next = jump_table[next.status_num].get(ch)

    if dfa_in_group(goto_first) != dfa_in_group(goto_next):
        new_group = DfaGroup()
        group_list.append(new_group)
        group.remove(next)
        new_group.add(next)
        return True

    return False


def dfa_in_group(status_num):
    for group in group_list:
        for dfa in group.group:
            if dfa.status_num == status_num:
                return group
    return None


def create_mindfa_table(jump_table):
    trans_table = list_dict(ASCII_COUNT)
    for dfa in dfa_list:
        from_dfa = dfa.status_num
        for i in range(ASCII_COUNT):
            ch = chr(i)
            to_dfa = jump_table[from_dfa].get(ch)
            if to_dfa:
                from_group = dfa_in_group(from_dfa)
                to_group = dfa_in_group(to_dfa)
                trans_table[from_group.group_num][ch] = to_group.group_num
                if dfa_list[from_dfa].accepted:
                    trans_table[from_group.group_num]['accepted'] = True
        print(trans_table)

    log_group(group_list)
    # print(trans_table)
    return trans_table


def print_group(group_list):
    for group in group_list:
        for dfa in group.group:
            print('******group ', group.group_num, dfa.status_num)


def log_group(group_list):
    for group in group_list:
        print('group num: ', group.group_num)
        for g in group.group:
            print('    dfa sets: ', g.status_num)