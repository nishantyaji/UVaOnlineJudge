import sys

num_inputs = int(sys.stdin.readline().strip())

for i in range(num_inputs):
    sys.stdin.readline()
    cols = int(sys.stdin.readline().strip())
    st = set()
    for c in range(cols):
        [a, b] = list(map(int, sys.stdin.readline().strip().split()))
        st.add(abs(a - b) + 1)

    if i > 0:
        print()
    print("yes" if len(st) == 1 else "no")
