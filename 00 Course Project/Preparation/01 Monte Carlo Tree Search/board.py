class Board:
    def __init__(self) -> None:
        self.board = [[0] * 3 for _ in range(3)]
        self.turn = 1 # 1 for X, -1 for O

    def make_move(self, player: int, coord: tuple[int, int]) -> None:
        self.board[coord[0] - 1][coord[1] - 1] = player
        if self.turn == 1:
            self.turn = -1
        elif self.turn == -1:
            self.turn = 1
            
    def is_player_winning(self, player: int) -> bool:
        if player not in [1, -1]:
            return ValueError('Player must be 1 or -1')
        for row in self.board:
            if all(cell == player for cell in row):
                return True

        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True

        if all(self.board[i][i] == player for i in range(3)):
            return True

        if all(self.board[i][2 - i] == player for i in range(3)):
            return True

        return False
    
    def get_empty_squares(self) -> list[tuple[int, int]]:
        res = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    res.append((i + 1, j + 1))
        return res
    
    def get_heuristic_value(self) -> int:
        winner = 0
        if self.is_player_winning(-1):
            winner = -1
        elif self.is_player_winning(1):
            winner = 1
        if winner == 0:
            raise ValueError('You can get a heuristic value only if the state is final')
        
        return winner * (1 + len(self.get_empty_squares()))
    
    def is_terminal(self) -> bool:
        return self.is_player_winning(-1) or self.is_player_winning(1)
        
    def __str__(self) -> str:
        symbols = {1: 'X', -1: 'O', 0: ' '}
        
        rows = []
        for row in self.board:
            row_str = " | ".join(symbols[cell] for cell in row)
            rows.append(row_str)
        
        board_str = "\n---------\n".join(rows)
    
        return board_str
        