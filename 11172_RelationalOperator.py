import sys

num_tests = int(sys.stdin.readline().strip())

for _ in range(num_tests):
    [a, b] = list(map(int, sys.stdin.readline().strip().split()))
    if a == b:
        print("=")
    elif a > b:
        print(">")
    else:
        print("<")
