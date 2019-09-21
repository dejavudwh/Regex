from nfa.nfa import EPSILON


def complier(start_node):
    pass


def closure(input_set):
    if not input_set:
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
            if next2 not in input_set:4
                input_set.append(next2)
                input_set.append(next2)

    return input_set
