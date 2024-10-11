import sys

num_inputs = int(sys.stdin.readline().strip())

acc = 0
for _ in range(num_inputs):
    s = sys.stdin.readline().strip().split()
    if len(s) == 1:
        print(acc)
    else:
        acc += int(s[1])
