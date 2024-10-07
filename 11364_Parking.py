# https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=2349

import sys

num_tests = int(sys.stdin.readline().strip())

for _ in range(num_tests):
    num_stores = int(sys.stdin.readline().strip())
    s = list(map(int, sys.stdin.readline().strip().split()))
    min_, max_ = sys.maxsize, -1
    for sx in s:
        min_ = min(min_, sx)
        max_ = max(max_, sx)
    print(2 * (max_ - min_))
