# https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=4&page=show_problem&problem=208
import sys

"""
Note that this is not a single line input.
The input might be a paragraph where the sentence
spans many lines.
We need to maintain whether `` or '' must be used
across different lines.
"""

flag = 0
replace = ["``", "''"]
for s in sys.stdin.readlines():
    res = ""
    for c in s:
        if c == "\"":
            res += replace[flag]
            flag ^= 1
        else:
            res += c
    sys.stdout.write(res)
