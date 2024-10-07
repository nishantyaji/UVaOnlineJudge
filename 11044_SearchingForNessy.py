# https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=1985
import math
import sys

num_tests = int(sys.stdin.readline().strip())

for _ in range(num_tests):
    [r, c] = list(map(int, sys.stdin.readline().strip().split()))
    print(math.ceil((r - 2) / 3) * math.ceil((c - 2) / 3))
