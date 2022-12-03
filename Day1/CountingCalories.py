with open('CountingCalories.in') as file:
    data = [i for i in file.read().strip().split("\n")]
max = 0
max2 = 0    
max3 = 0    
count = 0
for item in data:
    if item == '':
        count = 0       
    else:
        num = int(item) )
        count += num    
    if count > max: 
        max3 = max2
        max2 = max
        max = count
    elif count > max2:
        max3 = max2
        max2 = count     
    elif count > max3:
        max3 = count    
print("Part 1 solution: ", max)
print("Part 2 solution: ", max+max2+max3)
