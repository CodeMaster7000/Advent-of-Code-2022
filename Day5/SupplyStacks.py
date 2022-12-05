from util import *
from copy import deepcopy

def parse(inp):
    a, b = superlines(inp)
    g = np.array([list(x) for x in a.splitlines()]).transpose()
    s = [[x for x in l if x != ' '] for l in g[1::4, -2::-1]]
    m = [nums(l) for l in b.splitlines()]
    return s, m
def move(s, amount, src, dst, rev=True):
    src -= 1
    dst -= 1
    m = s[src][-amount:]
    if rev:
        m = list(reversed(m))
    s[src] = s[src][:-amount]
    s[dst] += m
def ans(s):
    return ''.join(map(lambda l: l[-1], s))
def p1(inp):
    s, b = inp
    for x, y, z in b:
        move(s, x, y, z, True)
    return ans(s)
def p2(inp):
    s, b = inp
    for x, y, z in b:
        move(s, x, y, z, False)
    return ans(s)
def main():
    inp = parse(data())
    print(f"Part 1 solution: {p1(deepcopy(inp))}")
    print(f"Part 2 solution: {p2(inp)}")
if __name__ == "__main__":
    main()
