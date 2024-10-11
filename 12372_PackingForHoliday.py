import sys

num_tests = int(sys.stdin.readline().strip())

i = 1
for _ in range(num_tests):
    dims = list(map(int, sys.stdin.readline().strip().split()))
    flag = all(map(lambda x: x <= 20, dims))
    res = "good" if flag else "bad"
    print("Case %d: %s" % (i, res))
    i += 1
