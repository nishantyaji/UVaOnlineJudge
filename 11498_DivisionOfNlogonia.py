# https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=2493
import sys

while True:
    num_queries = int(sys.stdin.readline().strip())
    if num_queries == 0:
        sys.exit()
    [ox, oy] = list(map(int, sys.stdin.readline().strip().split()))
    for _ in range(num_queries):
        [x, y] = list(map(int, sys.stdin.readline().strip().split()))
        xx, yy = x - ox, y - oy
        if xx * yy == 0:
            print("divisa")
        elif xx > 0 and yy > 0:
            print("NE")
        elif xx < 0 < yy:
            print("NO")
        elif xx < 0 and yy < 0:
            print("SO")
        else:
            print("SE")
