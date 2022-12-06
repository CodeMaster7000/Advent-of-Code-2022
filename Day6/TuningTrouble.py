import sys
from copy import deepcopy

infile = sys.argv[1] if len(sys.argv)>1 else 'TuningTrouble.in'
data = open(infile).read()
lines = [x for x in data.split('\n')]
p1 = False
p2 = False

for i in range(len(data)):
    if (not p1) and i-3>=0 and len(set([data[i-j] for j in range(4)]))==4:
        print("Part 1 solution:",i+1)
        p1 = True
    if (not p2) and i-13>=0 and len(set([data[i-j] for j in range(14)]))==14:
        print("Part 2 solution:",i+1)
        p2 = True
