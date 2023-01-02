from nfa.nfa import (
    EPSILON,
    CCL,
)


def match(input_string, nfa_machine):
    start_node = nfa_machine

    current_nfa_set = [start_node]
    next_nfa_set = closure(current_nfa_set)

    for i, ch in enumerate(input_string):
        current_nfa_set = move(next_nfa_set, ch)
        next_nfa_set = closure(current_nfa_set)

        if next_nfa_set is None:
            return False

        if has_accepted_state(next_nfa_set) and i == len(input_string) - 1:
            return True

    return False


def closure(input_set):
    if len(input_set) <= 0:
        return None

    nfa_stack = []
    for i in input_set:
        nfa_stack.append(i)

    while len(nfa_stack) > 0:
        nfa = nfa_stack.pop()
        next1 = nfa.next_1
        next2 = nfa.next_2
        if next1 is not None and nfa.edge == EPSILON:
            if next1 not in input_set:
                input_set.append(next1)
                nfa_stack.append(next1)

        if next2 is not None and nfa.edge == EPSILON:
            if next2 not in input_set:
                input_set.append(next2)
                nfa_stack.append(next2)

    return input_set


def move(input_set, ch):
    out_set = []
    for nfa in input_set:
        if nfa.edge == ch or (nfa.edge == CCL and ch in nfa.input_set):
            out_set.append(nfa.next_1)

    return out_set


def has_accepted_state(nfa_set):
    for nfa in nfa_set:
        if nfa.next_1 is None and nfa.next_2 is None:
            return True
