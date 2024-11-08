
from point import Point

class Path:
    def __init__(self, path: list[Point]):
        self.path = path
        self.distance = self._get_distance()
        
    def _get_distance(self) -> float:
        total: float = 0
        last: Point = self.path[0]
        for i in range(1, len(self.path)):
            total += last.get_distance(self.path[i])
            last = self.path[i]
        return total
    