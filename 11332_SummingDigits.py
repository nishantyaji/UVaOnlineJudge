import sys


def summ(numm):
    sm = sum(list(map(int, list(str(numm)))))
    if sm > 9:
        return summ(sm)
    return sm


while True:
    num = int(sys.stdin.readline().strip())
    if num == 0:
        sys.exit()
    print(summ(num))
