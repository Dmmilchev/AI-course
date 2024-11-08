import random

random.seed(42)

class Board:
    def __init__(self, N: int) -> None:
        self.N = N
        self.board = [-1] * self.N
        self.q_row = [0] * self.N
        self.q_d1 = [0] * (2 * self.N - 1)
        self.q_d2 = [0] * (2 * self.N - 1)
        self._board_init()
        
    def _board_init(self) -> None:
        for col in range(self.N):
            row = self.get_row_with_min_conflicts_without_queen(col)
            self.put_queen_on_coord((row, col))
        
    def remove_queen_on_col(self, col: int) -> None:
        row = self.board[col]
        self.q_row[row] -= 1
        self.q_d1[row - col + self.N - 1] -= 1
        self.q_d2[row + col] -= 1
        
    def put_queen_on_coord(self, coord: tuple[int, int]) -> None:
        row, col = coord
        self.board[col] = row
        self.q_row[row] += 1
        self.q_d1[row - col + self.N - 1] += 1
        self.q_d2[row + col] += 1
        
    def get_row_with_min_conflicts_without_queen(self, col: int) -> int:
        min = float('inf')
        rows = []
        for row in range(self.N):
            current = self.q_row[row] + self.q_d1[row - col + self.N - 1] + self.q_d2[row + col]

            if min > current:
                rows = [row]
                min = current
            elif min == current:
                rows.append(row)
                min = current
                
        return rows[0] if len(rows) == 0 else random.choice(rows)
    
    def get_row_with_min_conflicts(self, col: int) -> int:
        min = float('inf')
        rows = []
        for row in range(self.N):
            current = self.q_row[row] + self.q_d1[row - col + self.N - 1] + self.q_d2[row + col] - 3

            if min > current:
                rows = [row]
                min = current
            elif min == current:
                rows.append(row)
                min = current
                
        return rows[0] if len(rows) == 0 else random.choice(rows)
    
    def get_column_with_max_conflicts(self) -> int:
        cols = []
        max = float('-inf')
        
        for col in range(self.N):
            row = self.board[col]
            current = self.q_row[row] + self.q_d1[row - col + self.N - 1] + self.q_d2[row + col] - 3

            if current > max:
                cols = [col]
                max = current
            elif current == max:
                cols.append(col)
        
        return max, cols[0] if len(cols) == 0 else random.choice(cols)
    
    def __str__(self) -> str:
        m = [[0]* self.N for _ in range(self.N)]
        for col in range(self.N):
            row = self.board[col]
            if row > -1:
                m[row][col] = 1
        res = ''
        for i in range(self.N):
            for j in range(self.N):
                if m[i][j] == 1:
                    res += '* '
                else:
                    res += '_ '
            res += '\n'
        return res
