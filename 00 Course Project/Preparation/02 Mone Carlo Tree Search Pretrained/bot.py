from board import Board
from node import Node
import random
from copy import deepcopy

class Bot:
    PRETRAIN_GAMES = 1
    
    def __init__(self, player: int) -> None:
        if player not in [-1, 1]:
            raise ValueError('Player is 1 or -1')
        self.player = player
        
    def get_best_move(self, board: Board):
        if board.turn != self.player:
            raise ValueError('It is not bot\'s turn')
        
        pass
    
    def play_random_game(self, start: Node, tree: dict) -> tuple[float, list[tuple[int, int]]]:
        parent = start
        possible_moves = parent.board.get_empty_squares()
        path = []
                
        while possible_moves:
            move = random.choice(possible_moves)
            child = deepcopy(parent)
            child.board.make_move(child.board.turn, move)
            path.append(child)
            if child not in tree[parent]:
                tree[parent].add(child)
            possible_moves = child.board.get_empty_squares()
            
            if child not in tree.keys():
                tree[child] = set()

            if child.board.is_terminal():
                result = child.board.get_result()
                score = result * ((len(child.board.get_empty_squares()) + 1) / 10)
                return score, path
            
            parent = child

    # def _update_tree(self, score: float, moves: list[tuple[int, int]], tree: Node) -> None:
    #     for move in moves:
    #         board = deepcopy(tree.board)
    #         board.make_move(board.turn, move)
            
    #         found = False
    #         node = None
    #         if tree.children != None:
    #             for child in tree.children:
    #                 if child.board == board:
    #                     found = True
    #                     node = child
    #                     break
            
    #         if found:
    #             node.score += score
    #         else:
    #             n = Node(board, score)
    #             tree.children = set()
    #             tree.children.add(n)
        
    def pretrain(self) -> Node:
        board = Board()
        tree = dict()
        tree[board] = set()     
        for _ in range(Bot.PRETRAIN_GAMES):
            score, moves = self.play_random_game(board, tree)
            
        return tree
        
b = Bot(1)
tree = b.pretrain()
for key, value in tree.items():
    print('parent')
    print(str(key))
    print('children')
    for c in value:
        print(str(c))