from board import Board
from copy import deepcopy
import random

class Bot:
    NUMBER_OF_SIMULATION = 200
    
    def __init__(self, player: int) -> None:
        self.player = player
        
    def get_best_move(self, board: Board) -> tuple[int, int]:
        d = dict()
        
        for _ in range(Bot.NUMBER_OF_SIMULATION):
            result, move, empty_squares = self.is_winning_random_game(board)
            score = result * empty_squares
            if move not in d.keys():
                d[move] = score
            else:
                d[move] += score
        
        return max(d, key=d.get)
            
            
    def is_winning_random_game(self, board: Board) -> tuple[int, tuple[int, int], int]:
        player = board.turn
        
        board = deepcopy(board)
        possible_moves = board.get_empty_squares()
        moves_played = []
        while possible_moves:
            move = random.choice(possible_moves)
            moves_played.append(move)
            board.make_move(board.turn, move)
            if board.is_player_winning(player):
                return 1, moves_played[0], board.get_empty_squares()
            elif board.is_player_winning(1 if player == -1 else -1):
                return -1, moves_played[0], board.get_empty_squares()
            possible_moves = board.get_empty_squares()
            
        return 0, moves_played[0], board.get_empty_squares()
            