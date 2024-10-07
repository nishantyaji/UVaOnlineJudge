# https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=2827

import sys

num_tests = int(sys.stdin.readline().strip())

for i in range(num_tests):
    salaries = list(map(int, sys.stdin.readline().strip().split()))
    salaries.sort()
    print("Case %d: %d" % (i+1, salaries[1]))
