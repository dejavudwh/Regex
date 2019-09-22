from nfa.nfa import (
    EPSILON,
    CCL,
)
from nfa.construction import pattern


def match(input_string, pattern_string):
    start_node = pattern(pattern_string)

    current_nfa_set = [start_node]
    next_nfa_set = closure(current_nfa_set)

    for i, ch in enumerate(input_string):
        current_nfa_set = move(next_nfa_set, ch)
        # print('out move: ', current_nfa_set)
        next_nfa_set = closure(current_nfa_set)
        # print('out closure: ', next_nfa_set)

        if next_nfa_set is None:
            return False

        if has_accepted_state(next_nfa_set) and i == len(input_string) - 1:
            return True

    return False


def closure(input_set):
    # print('come in sure', input_set)
    if len(input_set) <= 0:
        return None

    nfa_stack = []
    for i in input_set:
        nfa_stack.append(i)

    while len(nfa_stack) > 0:
        nfa = nfa_stack.pop()
        next1 = nfa.next_1
        next2 = nfa.next_2
        # print('now: ', nfa.status_num, nfa.edge)
        if next1 is not None and nfa.edge == EPSILON:
            if next1 not in input_set:
                # print('closure add:', next1.status_num)
                input_set.append(next1)
                nfa_stack.append(next1)

        if next2 is not None and nfa.edge == EPSILON:
            if next2 not in input_set:
                # print('closure add:', next2.status_num)
                input_set.append(next2)
                nfa_stack.append(next2)
        
    # print('debug closure ***', input_set)
    return input_set


def move(input_set, ch):
    out_set = []
    for nfa in input_set:
        # print('debug move no 1****', ch, nfa.status_num, nfa.edge, nfa.input_set)
        if nfa.edge == ch or (nfa.edge == CCL and ch in nfa.input_set):
            # print('debug in move 1****', ch, nfa.status_num, nfa.edge, nfa.input_set)
            out_set.append(nfa.next_1)

    # print('debug move 2****', out_set)
    return out_set


def has_accepted_state(nfa_set):
    for nfa in nfa_set:
        if nfa.next_1 is None and nfa.next_2 is None:
            print('fuck******* ', nfa.status_num)
            return True
