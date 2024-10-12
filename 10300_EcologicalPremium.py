import sys

num_inputs = int(sys.stdin.readline().strip())

for _ in range(num_inputs):
    num_farmers = int(sys.stdin.readline().strip())
    res = 0
    for x in range(num_farmers):
        ins = list(map(int, sys.stdin.readline().strip().split()))
        res += (ins[0] * ins[2])
    print(res)
