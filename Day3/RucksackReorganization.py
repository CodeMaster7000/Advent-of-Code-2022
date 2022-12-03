from util import *
def parse(inp):
    return lines(inp)
def prio(c):
    return 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(c) + 1
def intersect(xs):
    return set.intersection(*map(set, xs)).pop()
def p1(inp):
    return sum(prio(intersect(parts(rucksack, 2))) for rucksack in inp)
def p2(inp):
    return sum(prio(intersect(badge)) for badge in chunks(inp, 3))
def main():
    inp = parse(data())
    print(f"Part 1 solution: {p1(inp)}")
    print(f"Part 2 solution: {p2(inp)}")
if __name__ == "__main__":
    main()
