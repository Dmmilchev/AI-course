from board import Board

class Bot:
    def __init__(self, player: int):
        if player not in [1, -1]:
            raise ValueError("Player must be 1 (X) or -1 (O)")
        self.player = player

    def minimax(self, board: Board, depth: int, alpha: int, beta: int, maximizing: bool) -> tuple[int, tuple[int, int]]:
        if board.is_terminal() or not board.get_empty_squares():
            if board.is_player_winning(self.player):
                return board.get_heuristic_value(), None 
            elif board.is_player_winning(-self.player):
                return board.get_heuristic_value(), None 
            else:
                return 0, None  

        best_move = None
        if maximizing:
            max_eval = -float('inf')
            for move in board.get_empty_squares():
                board.make_move(self.player, move)
                
                eval_score, _ = self.minimax(board, depth + 1, alpha, beta, False)
                
                board.make_move(0, move)
                
                if eval_score > max_eval:
                    max_eval = eval_score
                    best_move = move

                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break
            
            return max_eval, best_move

        else:
            min_eval = float('inf')
            for move in board.get_empty_squares():
                board.make_move(-self.player, move)
                
                eval_score, _ = self.minimax(board, depth + 1, alpha, beta, True)
                
                board.make_move(0, move)
                
                if eval_score < min_eval:
                    min_eval = eval_score
                    best_move = move

                beta = min(beta, eval_score)
                if beta <= alpha:
                    break

            return min_eval, best_move

    def get_best_move(self, board: Board) -> tuple[int, int]:
        _, best_move = self.minimax(board, depth=0, alpha=-float('inf'), beta=float('inf'), maximizing=True)
        return best_move
