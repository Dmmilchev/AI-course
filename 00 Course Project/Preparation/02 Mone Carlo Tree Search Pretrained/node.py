from board import Board

class Node:
    def __init__(self, board: Board, score: int, children: set = None) -> None:
        self.board = board
        self.score = score
        