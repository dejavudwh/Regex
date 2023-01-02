from dfa.dfa_group import DfaGroup
from nfa.nfa import ASCII_COUNT
from utils import list_dict
from utils import G


def minimize_dfa(jump_table):
    G.group_list = []
    G.on_partition = True
    partition_accepted()

    while G.on_partition:
        G.on_partition = False
        partition_on_num(jump_table)
        partition_on_char(jump_table)

    return create_mindfa_table(jump_table)


def partition_accepted():
    group_na = []
    group_a = []
    for dfa in G.dfa_list:
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
    G.group_list.append(group)


def partition_on_num(jump_table):
    for group in G.group_list:
        for i in range(10):
            divide_group = dict()
            for dfa in group.group:
                ch = str(i)
                partition(jump_table,  dfa, divide_group, ch)
            if len(divide_group) > 1:
                G.on_partition = True
                G.group_list.remove(group)
                add_group_list(G.group_list, divide_group.items())
                return


def add_group_list(group_list, divide_list):
    for item in divide_list:
        value_group = DfaGroup()
        value_group.group = item[1]
        group_list.append(value_group)


def partition_on_char(jump_table):
    for group in G.group_list:
        for i in range(ASCII_COUNT):
            divide_group = dict()  # divide_group的key是group_num,value是一个group中转向编号为group_num的dfa列表
            for dfa in group.group:
                ch = chr(i)
                partition(jump_table,  dfa, divide_group, ch)
            if len(divide_group) > 1:  # 字符ch将一个group划分成多个
                G.on_partition = True
                G.group_list.remove(group)
                add_group_list(G.group_list, divide_group.items())
                return


def partition(jump_table,  dfa, divide_group, ch):
    goto = jump_table[dfa.status_num].get(ch)
    goto_group = dfa_in_group(goto)
    if goto_group is None:
        if divide_group.get(-1) is None:
            divide_group[-1] = []
        divide_group[-1].append(dfa)
    else:
        if divide_group.get(goto_group.group_num) is None:
            divide_group[goto_group.group_num] = []
        divide_group[goto_group.group_num].append(dfa)


def dfa_in_group(status_num):
    for group in G.group_list:
        for dfa in group.group:
            if dfa.status_num == status_num:
                return group
    return None


def create_mindfa_table(jump_table):
    trans_table = list_dict(ASCII_COUNT)
    for dfa in G.dfa_list:
        from_dfa = dfa.status_num
        for i in range(ASCII_COUNT):
            ch = chr(i)
            to_dfa = jump_table[from_dfa].get(ch)
            if to_dfa:
                from_group = dfa_in_group(from_dfa)
                to_group = dfa_in_group(to_dfa)
                trans_table[from_group.group_num][ch] = to_group.group_num
        if dfa.accepted:
            from_group = dfa_in_group(from_dfa)
            trans_table[from_group.group_num]['accepted'] = True

    return trans_table


def print_group(group):
    for g in group.group:
        print('    dfa sets: ', g.status_num)


def log_group(group_list):
    for group in group_list:
        print('group num: ', group.group_num)
        for g in group.group:
            print('    dfa sets: ', g.status_num)
