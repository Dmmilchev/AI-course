from __future__ import annotations
from board import Board

class Node:
    def __init__(self, board: Board, parent: Node = None) -> None:
        self.board: Board = board
        self.parent: Node = parent
        self.visits: int = 0
        self.score: float = 0
        self.children: set[Node] = set()
        
        if board.is_terminal():
            self.is_expanded = True
        else:
            self.is_expanded = False
            
    def is_leaf(self) -> bool:
        return len(self.children) == 0
    
    def __eq__(self, other) -> bool:
        if self.parent is not None and other.parent is not None:
            return self.board == other.board and self.parent.board == other.parent.board
        elif self.parent is None and other.parent is None:
            return self.board == other.board
        else:
            return False
        
    def __hash__(self):
        if self.parent is not None:
            return hash((self.board, self.parent.board))
        else:
            return hash(self.board)
