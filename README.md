# Regex

![](https://img.shields.io/badge/language-Python-blue.svg)
![](https://img.shields.io/badge/category-learning-yellow.svg)
[![](https://img.shields.io/badge/blog-@dejavudwh-red.svg)](https://dejavudwh.cn/)
![](http://progressed.io/bar/82?title=done)

> *This is a regular expression engine implemented in Python that uses NFA and DFA and optionally minimizes DFA sets*.

# Begin to use

```python
from regex import Regex


st = 'THISISREGEXTEST'
pattern = '([A-Z]*|[0-9]+)'
regex = Regex(st, pattern)
result = regex.match()
log(result)
```

Regex build parameter
```python
(input_string, pattern_string, mode=1, minimize=True)
```

- ### mode

    Finite state automata used

    mode = 1 - NFA

    mode = 2 - DFA

- ### minimize

    Whether to minimize if using DFA


**see sample.py for details**.

# BNF

```python
group ::= ("(" expr ")")*
expr ::= factor_conn ("|" factor_conn)*
factor_conn ::= factor | factor factor*
factor ::= (term | term ("*" | "+" | "?"))*
term ::= char | "[" char "-" char "]" | .
```

# Implementation of the

> Implemented all the basic syntax

```python
Tokens = {
    '.': Token.ANY,
    '^': Token.AT_BOL,
    '$': Token.AT_EOL,
    ']': Token.CCL_END,
    '[': Token.CCL_START,
    '}': Token.CLOSE_CURLY,
    ')': Token.CLOSE_PAREN,
    '*': Token.CLOSURE,
    '-': Token.DASH,
    '{': Token.OPEN_CURLY,
    '(': Token.OPEN_PAREN,
    '?': Token.OPTIONAL,
    '|': Token.OR,
    '+': Token.PLUS_CLOSE,
}
```
*in lex.token*

## Code structure

> For the sake of simplicity, the code style of this implementation is not very good.

- ### lex
    Lexical analysis of regular expressions
- ### nfa
    Definition of an NFA node the construction of an NFA
- ### dfa
    Definition of an DFA node the construction of an DFA
- ### parse
    About parsing DFA or NFA based on input

