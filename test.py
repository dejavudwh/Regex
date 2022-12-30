import unittest
from regex import Regex

class RegexMaterial(object):
    def __init__(self, str, pattern, result):
        self.str = str
        self.pattern = pattern
        self.result = result

testLists = []
testLists.append(RegexMaterial("a", "a", True))
testLists.append(RegexMaterial("a", "b+", False))
testLists.append(RegexMaterial("b", "b+", True))
testLists.append(RegexMaterial("ab", "(ab|cd)", True))
testLists.append(RegexMaterial("THISISREGEXTEST", "([A-Z]*|[0-9]+)", True))
testLists.append(RegexMaterial("abbbbb", "[^c]+", True))
testLists.append(RegexMaterial("ccccc", "[^c]+", False))
testLists.append(RegexMaterial("123", "[1-3]+", True))
testLists.append(RegexMaterial("^", "[^1-3]+", True))

class TestRegex(unittest.TestCase):
    def test(self):
        for t in testLists:
            print("str is " + t.str + ", pattern is " + t.pattern + ", expected " + str(t.result))
            regex = Regex(t.str, t.pattern)
            self.assertEqual(regex.match(), t.result)



if __name__ == '__main__':
    unittest.main()