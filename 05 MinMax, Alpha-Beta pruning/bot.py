from board import Board

class Bot:
    def __init__(self, player: int) -> None:
        if player not in [1, -1]:
            raise ValueError('Player must be 1 or -1')
        self.player = player
        
    def move(self, 
             board: Board, 
             depth: int, 
             alpha: int, 
             beta: int, maximizingPlayer: bool):
        
        if depth == 0 or board.is_terminal():
            return board.get_heuristic_value()
        
        if maximizingPlayer:
            val = float('-inf')
            for move in board.get_empty_squares():
                board.make_move(1, move)
                val = max(val, self.move(board, depth - 1, alpha, beta, False)[0])
                alpha = max(val, alpha)
                board.make_move(0, move)
                if val >= beta:
                    break
                return val, move
            
        else:
            val = float('inf')
            for move in board.get_empty_squares():
                board.make_move(-1, move)
                val = max(val, self.move(board, depth - 1, alpha, beta, True)[0])
                beta = min(val, beta)
                board.make_move(0, move)
                if val <= alpha:
                    break
                return val, move