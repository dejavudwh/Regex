MAX_DFA_STATUS_NUM = 256


class Dfa(object):
    STATUS_NUM = 0

    def __init__(self):
        self.nfa_sets = []
        self.accepted = False
        self.status_num = -1

    @classmethod
    def nfas_to_dfa(cls, nfas):
        print('come in to**')
        dfa = cls()
        for n in nfas:
            dfa.nfa_sets.append(n)
            print('nfa status num **********', n.status_num)
            if n.next_1 is None and n.next_2 is None:
                print('is accepted ************* ', n.status_num)
                dfa.accepted = True

        dfa.status_num = Dfa.STATUS_NUM
        Dfa.STATUS_NUM = Dfa.STATUS_NUM + 1
        return dfa