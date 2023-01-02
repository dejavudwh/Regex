from regex import Regex
from utils import log


# TRUE
st = 'THISISREGEXTEST'
pattern = '([A-Z]*|[0-9]+)'

# FALSE
st = 'THISISREGEXTEST'
pattern = '([A-Z]+[0-9]+)'

# FALSE
st = '234234abcdefg[*+'
pattern = '([A-Z]+[0-9]*abcdefg)(\[\*\+)'

# TRUE
st = 'AS342abcdefg234aaaaabccccczczxczcasdzxc'
pattern = '([A-Z]+[0-9]*abcdefg)([0-9]*)(\*?|a+)(zx|bc*)([a-z]+|[0-9]*)(asd|fgh)(zxc)'


# NFA
regex = Regex(st, pattern)
result = regex.match()
log(result)


# DFA MINIMIZE
regex = Regex(st, pattern, 2)
result = regex.match()
log(result)


# DFA NO MINIMIZE
regex = Regex(st, pattern, 2, False)
result = regex.match()
log(result)
