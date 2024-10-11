import sys

i = 1
my_dict = {"Hajj": "Hajj-e-Akbar", "Umrah": "Hajj-e-Asghar"}
while True:
    inp = sys.stdin.readline().strip()
    if inp == "*":
        sys.exit()
    print("Case %d: %s" % (i, my_dict[inp]))
    i += 1
