from __future__ import annotations
from copy import deepcopy

class Board:
    def __init__(self) -> None:
        self.board = [[0] * 3 for _ in range(3)]
        self.turn = 1 # 1 for X, -1 for O

    def _make_move(self, coord: tuple[int, int]) -> None:
        self.board[coord[0] - 1][coord[1] - 1] = self.turn
        if self.turn == 1:
            self.turn = -1
        elif self.turn == -1:
            self.turn = 1
            
    def get_states(self) -> list[Board]:
        states: list[Board] = []
        for move in self.get_empty_squares():
            b = deepcopy(self)
            b._make_move(move)
            states.append(b)
        return states
            
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
    
    def is_win(self) -> bool:
        return self.is_player_winning(-1) or self.is_player_winning(1)

    def is_draw(self) -> bool:
        return not self.is_win() and len(self.get_empty_squares()) == 0
    
    def is_terminal(self) -> bool:
        return  self.is_win() or self.is_draw()
        
    def get_score(self) -> float:
        if self.is_draw():
            return 0
        elif self.is_player_winning(1):
            return 1 + len(self.get_empty_squares())
        elif self.is_player_winning(-1):
            return -1 - len(self.get_empty_squares())
        else:
            raise ValueError('This is not a terminal state, can not get score for it')
        
    def __str__(self) -> str:
        symbols = {1: 'X', -1: 'O', 0: ' '}
        
        rows = []
        for row in self.board:
            row_str = " | ".join(symbols[cell] for cell in row)
            rows.append(row_str)
        
        board_str = "\n---------\n".join(rows)
    
        return board_str
    
    def __eq__(self, other) -> bool:
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != other.board[i][j]:
                    return False
        return self.turn == other.turn
    
    def __hash__(self):
        board_tuple = tuple(tuple(row) for row in self.board)
        return hash((board_tuple, self.turn))        
    