import sys

base = 40
rotation = 360
multipliers = rotation // base

"""
Note that if you turn the lock in clockwise direction
the number decreases
(A bit counter intuitive at first glance)
"""
def diff_(source, dest):
    # This assumes clockwise
    # where source is usually higher than dest
    # if source is 30 and dest is 20 then degrees is 90 (and not 270)
    if source < dest:
        return source * multipliers + rotation - dest * multipliers
    return source * multipliers - dest * multipliers


while True:
    s = sys.stdin.readline().strip()
    if s == "0 0 0 0":
        sys.exit()
    ins = list(map(int, s.split()))
    res = 2 * rotation
    res += diff_(ins[0], ins[1])
    res += rotation
    res += (rotation - diff_(ins[1], ins[2])) # this is anti-clockwise
    res += diff_(ins[2], ins[3])
    # use print instead of sys.stdout.write, so that every new print is
    # in a new line
    print(str(res))
