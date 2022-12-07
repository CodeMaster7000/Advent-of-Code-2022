with open('TuningTrouble.in') as file: 
     input = file.read() 
 for i in range(4, len(input)): 
     s = set(input[(i-4):i]) 
     if len(s) == 4: 
         print("Part 1 solution: ", i) 
         break 
 for i in range(14, len(input)): 
     s = set(input[(i-14):i]) 
     if len(s) == 14: 
         print("Part 2 solution: ", i) 
         break
