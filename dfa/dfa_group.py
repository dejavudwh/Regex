class DfaGroup(object):
    GROUP_COUNT = 0

    def __init__(self):
        self.set_count()
        self.group = []

    def set_count(self):
        self.group_num = DfaGroup.GROUP_COUNT
        DfaGroup.GROUP_COUNT = DfaGroup.GROUP_COUNT + 1

    def remove(self, element):
        self.group.remove(element)

    def add(self, element):
        self.group.append(element)

    def get(self, count):
        if count > len(self.group) - 1:
            return None
        return self.group[count]