import math

class Point:
    def __init__(self, x: int, y: int, name: str = None) -> None:
        self.x = x
        self.y = y
        self.name = name
        
    def get_distance(self,  other) -> float:
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    
    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y
    