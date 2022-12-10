with open("Cathode-RayTube.in") as file:
    X = 1 
    cycle = 0
    display = []
    row = ""
    cycles = set([20, 60, 100, 140, 180, 220])
    def is_matching(cycle):
        if cycle in cycles:
            return True
        return False
    strengths = 0 
    for line in file:
        instructions = line.rstrip().split()
        if instructions[0] == "noop":
            cycle += 1
            row += "#" if len(row) in range(X - 1, X + 2) else "."
            if len(row) == 40:
                display.append(row)
                row = ""
            if is_matching(cycle):
                strengths += (X * cycle)
        if instructions[0] == "addx":
            T = 2
            while T > 0:
                cycle += 1
                row += "#" if len(row) in range(X - 1, X + 2) else "."
                if len(row) == 40:
                    display.append(row)
                    row = ""
                if is_matching(cycle):
                    strengths += (X * cycle)
                T -= 1
            X += int(instructions[1])
    print("Part 1 solution:",strengths) 
    print("Part 2 solution:",*display, sep="\n") 
