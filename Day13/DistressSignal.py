from __future__ import annotations
from pathlib import Path
from ast import literal_eval
SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "DistressSignal.in")
class Packet():   
    def __init__(self, value) -> None:
        self.value = value        
    def __lt__(self, other: Packet) -> bool:
        if isinstance(self.value, int) and isinstance(other.value, int):
            if self.value < other.value:
                return True 
            if other.value < self.value:
                return False
        if isinstance(self.value, int) and isinstance(other.value, list):
            new_item = Packet([self.value]) 
            return new_item < other
        if isinstance(self.value, list) and isinstance(other.value, int):
            new_item = Packet([other.value]) 
            return self < new_item
        if isinstance(self.value, list) and isinstance(other.value, list):
            compare_count = 0
            for val in zip(self.value, other.value): 
                compare_count += 1
                if val[0] == val[1]:
                    continue
                return Packet(val[0]) < Packet(val[1])
            return len(self.value) < len(other.value)       
    def __repr__(self) -> str:
        return str(self.value)    
class Pair():
    def __init__(self, left: Packet, right: Packet) -> None:
        self.left = left
        self.right = right
    def __repr__(self):
        return f"Pair(l={self.left}, r={self.right})"
def main():
    with open(INPUT_FILE, mode="rt") as f:
        data = f.read()      
    pairs = get_pairs(data)
    right_order = []    
    for i, pair in enumerate(pairs, start=1):
        if pair.left < pair.right:
            right_order.append(i)      
    print(f"Part 1 solution: {sum(right_order)}")
    all_packets = get_all_packets(data)
    div_two, div_six = Packet([[2]]), Packet([[6]])
    all_packets.append(div_two)
    all_packets.append(div_six)
    sorted_items = sorted(all_packets)
    loc_div_two = sorted_items.index(div_two) + 1 
    loc_div_six = sorted_items.index(div_six) + 1
    print(f"Part 2 solution: {loc_div_two*loc_div_six}")
def get_pairs(data: str) -> list[Pair]:
    pairs: list[Pair] = []
    blocks = data.split("\n\n")  
    for block in blocks:
        lines = block.splitlines()
        pairs.append(Pair(Packet(literal_eval(lines[0])), Packet(literal_eval(lines[1]))))       
    return pairs
def get_all_packets(data: str) -> list[Packet]:
    lines = data.splitlines()
    return [Packet(literal_eval(line)) for line in lines if line]
