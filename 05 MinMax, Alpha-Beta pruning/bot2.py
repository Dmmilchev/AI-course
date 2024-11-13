from board import Board

class Bot:
    def __init__(self, player: int):
        """
        Initialize the Bot for a given player.
        
        Parameters:
        player (int): The player for whom this bot will make moves. 1 for 'X' and -1 for 'O'.
        """
        if player not in [1, -1]:
            raise ValueError("Player must be 1 (X) or -1 (O)")
        self.player = player

    def minimax(self, board: Board, depth: int, alpha: int, beta: int, maximizing: bool) -> tuple[int, tuple[int, int]]:
        """
        Minimax function with alpha-beta pruning to find the best move.
        
        Parameters:
        board (Board): The current board state.
        depth (int): The current depth in the search tree.
        alpha (int): The best value the maximizer can guarantee.
        beta (int): The best value the minimizer can guarantee.
        maximizing (bool): True if the current layer is maximizing, False if minimizing.
        
        Returns:
        tuple[int, tuple[int, int]]: The best score and the best move as a coordinate (row, col).
        """
        # Check if the board is in a terminal state (win or draw)
        if board.is_terminal() or not board.get_empty_squares():
            if board.is_player_winning(self.player):
                return board.get_heuristic_value(), None  # Win for the bot
            elif board.is_player_winning(-self.player):
                return board.get_heuristic_value(), None  # Loss for the bot
            else:
                return 0, None  # Draw

        # Initialize variables
        best_move = None
        if maximizing:
            max_eval = -float('inf')
            for move in board.get_empty_squares():
                # Make the move
                board.make_move(self.player, move)
                
                # Recursively call minimax for the opponent
                eval_score, _ = self.minimax(board, depth + 1, alpha, beta, False)
                
                # Undo the move
                board.make_move(0, move)
                
                # Check if this move is better than the best we found so far
                if eval_score > max_eval:
                    max_eval = eval_score
                    best_move = move

                # Update alpha and check for pruning
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break
            
            return max_eval, best_move

        else:
            min_eval = float('inf')
            for move in board.get_empty_squares():
                # Make the move
                board.make_move(-self.player, move)
                
                # Recursively call minimax for the bot's turn
                eval_score, _ = self.minimax(board, depth + 1, alpha, beta, True)
                
                # Undo the move
                board.make_move(0, move)
                
                # Check if this move is better than the best we found so far
                if eval_score < min_eval:
                    min_eval = eval_score
                    best_move = move

                # Update beta and check for pruning
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break

            return min_eval, best_move

    def get_best_move(self, board: Board) -> tuple[int, int]:
        """
        Get the best possible move for the bot on the given board.
        
        Parameters:
        board (Board): The current board state.
        
        Returns:
        tuple[int, int]: The best move as a coordinate (row, col).
        """
        # Call minimax with alpha-beta pruning to get the best move
        _, best_move = self.minimax(board, depth=0, alpha=-float('inf'), beta=float('inf'), maximizing=True)
        return best_move
