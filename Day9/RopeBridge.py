from sys import argv
def adjust(H,T):
    dr = (H[0]-T[0])
    dc = (H[1]-T[1])
    if abs(dr)>=2 and abs(dc)>=2:
        T = (H[0]-1 if T[0]<H[0] else H[0]+1, H[1]-1 if T[1]<H[1] else H[1]+1)
    elif abs(dr)>=2:
        T = (H[0]-1 if T[0]<H[0] else H[0]+1, H[1])
    elif abs(dc)>=2:
        T = (H[0], H[1]-1 if T[1]<H[1] else H[1]+1)
    return T
lines = open(argv[1] if len(argv)>1 else "RopeBridge.in").read().strip().split("\n")
H = (0, 0)
T = [(0, 0) for _ in range(9)]
dirs = {"U":(-1, 0), "R":(0, 1), "D":(1, 0), "L":(0, -1)}
posT = {(0, 0)}
pos9 = {(0, 0)}
for line in lines:
    Dir, Len = line.split()
    for _ in range(int(Len)):
        H = (H[0] + dirs[Dir][0], H[1] + dirs[Dir][1])
        T[0] = adjust(H, T[0])
        for i in range(1, 9):
            T[i] = adjust(T[i-1], T[i])
        posT.add(T[0])
        pos9.add(T[8])
print("Part 1 solution:", len(posT))
print("Part 2 solution:", len(pos9))   
