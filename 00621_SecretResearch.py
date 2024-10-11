import sys

num_inputs = int(sys.stdin.readline().strip())

pos = ["1", "4", "78"]
for _ in range(num_inputs):
    s = sys.stdin.readline().strip()
    if s in pos:
        print("+")
    elif s[::-1].startswith("53"):
        print("-")
    elif s.startswith("9") and s[::-1].startswith("4"):
        print("*")
    elif s.startswith("190"):
        print("?")