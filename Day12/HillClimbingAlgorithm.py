from __future__ import annotations
from collections import deque
from dataclasses import dataclass
from pathlib import Path
SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "HillClimbingAlgorithm.in")
@dataclass(frozen=True)
class Point():  
    x: int
    y: int
    def neighbours(self) -> list[Point]:
        return [Point(self.x+dx, self.y+dy) for dx in range(-1, 2)
                                            for dy in range(-1, 2)
                                            if abs(dy) != abs(dx)]
class Grid():
    def __init__(self, grid_array: list[str]) -> None:                                        
        self.array = grid_array  
        self.x_size = len(self.array[0])
        self.y_size = len(self.array)
        self.start = self._get_point_for_elevation("S")
        self.goal = self._get_point_for_elevation("E")        
    def _all_points(self) -> list[Point]:
        points = [Point(x, y) for x in range(self.x_size) for y in range(self.y_size)]
        return points    
    def all_lowest_elevation_points(self) -> set[Point]:
        low_points = {point for point in self._all_points() 
                        if self.array[point.y][point.x] == "a"
                        or self.array[point.y][point.x] == "S"}
        return low_points  
    def _get_point_for_elevation(self, x: str) -> Point:
        assert x in ("S", "E"), 
        for row_num, row in enumerate(self.array):
            if x in row:
                return Point(row.index(x), row_num)    
    def elevation_at_point(self, point: Point) -> int:
        if point not in (self.start, self.goal):
            return ord(self.array[point.y][point.x])       
        if point == self.start:
            return ord("a") 
        if point == self.goal:
            return ord("z") 
    def _point_in_grid(self, point: Point) -> bool:
        if (0 <= point.x < self.x_size and 0 <= point.y < self.y_size):
            return True       
        return False    
    def _valid_neighbours(self, location:Point):
        current_elevation = self.elevation_at_point(location)       
        for neighbour in location.neighbours():
            if self._point_in_grid(neighbour):
                if self.elevation_at_point(neighbour) <= current_elevation + 1:
                    yield neighbour
    def get_path(self, start: Point):
        points_to_assess: deque[Point] = deque()  
        points_to_assess.append(start)   
        came_from = {}
        came_from[start] = None        
        while points_to_assess:     
            current = points_to_assess.popleft()
            if current == self.goal:  
                break
            for neighbour in self._valid_neighbours(current):
                if neighbour not in came_from:   
                    points_to_assess.append(neighbour)
                    came_from[neighbour] = current
        if current != self.goal:
            return None 
        current = self.goal
        path = []
        while current != start: 
            path.append(current)
            current = came_from[current]       
        return path
    def __repr__(self) -> str:
        return "\n".join("".join(map(str, row)) for row in self.array)     
def main():
    with open(INPUT_FILE, mode="rt") as f:
        data = f.read().splitlines()      
    grid = Grid(data)
    path = grid.get_path(grid.start)
    p1_length = len(path)
    print(f"Part 1 solution: {p1_length}")
    start_points = grid.all_lowest_elevation_points()
    p2_length = p1_length
    for start in start_points:
        path = grid.get_path(start)
        if path:
            p2_length = min(p2_length, len(path))
    print(f"Part 2 solution: {p2_length}")
