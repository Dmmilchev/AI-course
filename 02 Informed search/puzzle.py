from copy import deepcopy

class Puzzle:
    MOVES = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    def __init__(self, k, l, m, initialize=True) -> None:
        if initialize:
            self.k = k
            self.l = l
            self.m = m
            self.goal_zero_position = (int(l/k), l%k)
            self.current_zero_position = self.get_current_zero_position()
            self.goal_matrix = self.get_goal_matrix()

    def get_goal_matrix(self):
        m = [[0] * self.k for _ in range(self.k)]
        el = 1
        for i in range(self.k):
            for j in range(self.k):
                m[i][j] = el
                el += 1
        m[self.goal_zero_position[0]][self.goal_zero_position[1]] = 0
        return m
        
    def get_current_zero_position(self):
        for i in range(self.k):
            for j in range(self.k):
                if self.m[i][j] == 0:
                    return i, j
        
    def is_goal(self) -> bool:
        for i in range(self.k):
            for j in range(self.k):
                if self.m[i][j] != self.goal_matrix[i][j]:
                    return False
        return True
    
    def move(self, move) -> bool:
        new_zero_position = list(self.current_zero_position)
        new_zero_position[0] += move[0]
        new_zero_position[1] += move[1]
        
        if new_zero_position[0] < 0 or new_zero_position[1] >= self.k or \
            new_zero_position[0] >= self.k or new_zero_position[1] < 0:
            return False
        
        # Swapping:
        self.m[new_zero_position[0]][new_zero_position[1]], \
        self.m[self.current_zero_position[0]][self.current_zero_position[1]] = \
        self.m[self.current_zero_position[0]][self.current_zero_position[1]], \
        self.m[new_zero_position[0]][new_zero_position[1]]
        self.current_zero_position = tuple(new_zero_position)
        
        return True
    
    # this got things 3 times faster
    def get_copy(self):
        copy = Puzzle(None, None, None, False)
        copy.m = deepcopy(self.m)
        copy.k = self.k
        copy.l = self.l
        copy.goal_zero_position = self.goal_zero_position
        copy.current_zero_position = self.current_zero_position
        copy.goal_matrix = self.goal_matrix
        return copy
  
    def try_move(self, direction) -> tuple:
        n = self.get_copy()
        return n.move(direction), n
    
    def h(self) -> int:
        total = 0
        for i in range(self.k):
            for j in range(self.k):
                goalPos = ((self.m[i][j] - 1)// self.k), ((self.m[i][j] - 1) % self.k)
                total += abs(goalPos[0] - i)
                total += abs(goalPos[1] - j)
        return total
    
    def __str__(self) -> str:
        res = ''
        for i in range(self.k):
            for j in range(self.k):
                res += f'{self.m[i][j]}  '
            res += '\n'
        return res
                
                
    def _count_inversions(self) -> int:
        arr = []
        for i in range(self.k):
            for j in range(self.k):
                if self.m[i][j] != 0:
                    arr.append(self.m[i][j])

        count = 0
        n = len(arr)
        
        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] > arr[j]:
                    count += 1
                    
        return count

    def is_solvable(self) -> bool:
        inversions = self._count_inversions()
        
        if self.k % 2 == 0:
            zero_row, _ = self.current_zero_position
            return (zero_row + inversions) % 2 == 1
        else:
            return inversions % 2 == 0