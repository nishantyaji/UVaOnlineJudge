# https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3402
import sys

lang_dict = {"HELLO": "ENGLISH", "HOLA": "SPANISH", "HALLO": "GERMAN", "BONJOUR": "FRENCH",
             "CIAO": "ITALIAN", "ZDRAVSTVUJTE": "RUSSIAN"}
i = 1
while True:
    s = sys.stdin.readline().strip()
    if s == "#":
        sys.exit()
    print("Case %d: %s" % (i, lang_dict[s] if s in lang_dict else "UNKNOWN"))
    i += 1