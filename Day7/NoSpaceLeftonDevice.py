from dataclasses import dataclass, field
from typing import List
from aoc import get_lines

TOTAL_SIZE = 70000000
SIZE_NEEDED = 30000000

@dataclass
class Node:
    name: str
    size: int = 0
    is_file: bool = False
    parent: 'Node' = None
    children: dict[str, 'Node'] = field(default_factory=dict)
    
def parse_input(lines):
    root = Node('/')
    cur_node = root
    for line in lines:
        tokenz = line.split()
        if line.startswith('$'):
            cur_node = parse_command(cur_node=cur_node, root=root, line=line, tokenz=tokenz)
        else:
            parse_ls_output(cur_node=cur_node, tokenz=tokenz)
    return root

def parse_ls_output(cur_node, tokenz):
    size_or_dir, name = tokenz[0], tokenz[1]
    if size_or_dir == 'dir' and name not in cur_node.children.keys():
        cur_node.children[name] = Node(name=name, parent=cur_node)
    elif name not in cur_node.children.keys():
        cur_node.children[name] = Node(name=name, size=int(size_or_dir), is_file=True, parent=cur_node)

def parse_command(cur_node: Node, root: Node, line: str, tokenz: List[str]) -> Node:
    if 'cd' in line:
        folder = tokenz[2]
        if folder == '..':
            return cur_node.parent
        if folder == '/':
            return root
        if folder not in cur_node.children.keys():
            cur_node.children[folder] = Node(folder)
        return cur_node.children[folder]
    if 'ls' in line:
        pass
    return cur_node

def calc_sum(node: Node, sizes: List[int]) -> (int, List[int]):
    if node.is_file:
        return node.size, sizes
    sizes.append(sum(calc_sum(child, sizes)[0] for child in node.children.values()))
    return sizes[-1], sizes

def part1(sizes: List[int]) -> int:
    return sum(filter(lambda x: x < 100000, sizes))

def part2(sizes: List[int], cur_used: int) -> int:
    needed = SIZE_NEEDED - (TOTAL_SIZE - cur_used)
    return min(filter(lambda x: x > needed, sizes))

def main():
    lines = get_lines("input_07.txt")
    cur_used, sizes = calc_sum(parse_input(lines), [])
    print("Part 1 solution: ", part_1(sizes))  
    print("Part 2 solution: ", part_2(sizes, cur_used))  

if __name__ == '__main__':
    main()
