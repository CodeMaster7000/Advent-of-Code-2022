import sys
from collections import defaultdict
infile = sys.argv[1] if len(sys.argv)>1 else 'NoSpaceLeftonDevice.in'
data = open(infile).read().strip()
lines = [x for x in data.split('\n')]
SZ = defaultdict(int)
path = []
for line in lines:
    words = line.strip().split()
    if words[1] == 'cd':
        if words[2] == '..':
            path.pop()
        else:
            path.append(words[2])
    elif words[1] == 'ls':
        continue
    elif words[0] == 'dir':
        continue
    else:
        sz = int(words[0])
        for i in range(1, len(path)+1):
            SZ['/'.join(path[:i])] += sz
max_used = 70000000 - 30000000
total_used = SZ['/']
need_to_free = total_used - max_used
p1 = 0
p2 = 1e9
for k,v in SZ.items():
    if v <= 100000:
        p1 += v
    if v>=need_to_free:
        p2 = min(p2, v)
print("Part 1 solution:",p1)
print("Part 2 solution:",p2)
