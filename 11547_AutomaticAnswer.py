# https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=2542
import sys

num_tests = int(sys.stdin.readline().strip())

for _ in range(num_tests):
    n = int(sys.stdin.readline().strip())
    n *= (567 // 9)
    n += 7492
    n *= (235 // 47)
    n -= 498
    n = abs(n)
    print(((n % 100) - (n % 10)) // 10)
