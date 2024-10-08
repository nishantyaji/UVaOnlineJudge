# https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=3431
import sys

i = 1
while True:
    num = int(sys.stdin.readline().strip())
    if num == 0:
        sys.exit()
    arr = list(map(int, sys.stdin.readline().strip().split()))
    res = num - 2 * sum([1 for i in arr if i == 0])
    print("Case %d: %s" % (i, res))
    i += 1
