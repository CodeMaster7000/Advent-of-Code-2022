import collections
import functools
import bisect
with open((__file__.rstrip("DistressSignal.py")+"DistressSignal.in"), 'r') as input_file:
    input = input_file.readlines()
def addToList(idx, str) -> tuple:
    res = collections.deque()
    while idx < len(str):
        if str[idx] == "[":
            newList = addToList(idx+1, str)
            idx = newList[0]
            res.append(newList[1])
        elif str[idx] == "]":
            return (idx, res)
        elif str[idx].isnumeric():
            s = str[idx]
            if str[idx + 1].isnumeric():
                s += str[idx + 1]
                idx += 1
            res.append(int(s))
        idx += 1
    return (len(str),res)
def compare_lists(vals1, vals2) ->int:
    while vals1 and vals2:
        val1 = vals1.popleft()
        val2 = vals2.popleft()
        if isinstance(val1, int) and isinstance(val2, int):
            if val1 < val2:
                return 1
            elif val1 > val2:
                return -1
        else:
            val1 = collections.deque([val1]) if isinstance(val1, int) else val1
            val2 = collections.deque([val2]) if isinstance(val2, int) else val2
            subList = compare_lists(val1, val2)
            if 0 != subList:
                return subList
    if vals1:
        return -1
    return 1 if vals2 else 0
def check_in_order(str1, str2):
    q1, q2 =addToList(0, str1)[1], addToList(0, str2)[1]
    return compare_lists(q1, q2)
res = 0
idx = 0
lines = []
for i in range(0, len(input), 3):
    idx += 1
    if check_in_order(input[i].strip(), input[i +1].strip()):
        res += idx
        lines.append(input[i].strip())
        lines.append(input[i+1].strip())
print("Part 1 solution: "+ str(res))
lines.append('[[2]]')
lines.append('[[6]]')
lines.sort(key=functools.cmp_to_key(check_in_order),reverse=True)
res = 1
for i, line in enumerate(lines):
    if line == '[[2]]' or line == '[[6]]':
        res *= (i + 1)
print("Part 2 solution: "+ str(res))
