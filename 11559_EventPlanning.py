import sys

while True:
    try:
        [n, b, h, w] = list(map(int, input().strip().split()))
    except:
        # this is essential to go to the end of the input file
        break
    p, a = [], []
    for _ in range(h):
        p.append(int(input().strip()))
        a.append(list(map(int, input().strip().split())))

    min_ = sys.maxsize
    for i in range(h):
        sm = sum([1 for ax in a[i] if ax >= n])
        if sm:
            min_ = min(min_, n * p[i])

    if min_ > b:
        print("stay home")
    else:
        print(min_)
