# https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3710
import operator
import sys

num_tests = int(sys.stdin.readline().strip())


def calc_score(given, ref):
    if len(given) != len(ref):
        return 0
    match = sum([1 for i in range(len(given)) if given[i] == ref[i]])
    return match / len(given)


words = ["one", "two", "three"]
for _ in range(num_tests):
    s = sys.stdin.readline().strip()
    temp = [(i + 1, calc_score(s, words[i])) for i in range(len(words))]
    temp.sort(key=operator.itemgetter(1), reverse=True)
    print(temp[0][0])
