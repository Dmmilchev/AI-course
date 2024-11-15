from board import Board
from node import Node
import random
import math

class Bot:
    SIMULATIONS = 10000
    
    def __init__(self, exploration_constant: float = math.sqrt(2)) -> None:
        self.exploration_constant = exploration_constant
        
        
    def get_UCB1(self, node: Node) -> float:
        if node.visits == 0:
            return float('inf')
        N = 0 if node.parent is None else node.parent.visits
        return node.score / node.visits + self.exploration_constant * (math.sqrt(math.log(N) / node.visits))
        
    def get_best_move(self, initial_state: Board):
        self.root = Node(initial_state)
        
        for _ in range(Bot.SIMULATIONS):
            current = self.root
            
            while not current.is_leaf() and not current.board.is_terminal():
                maximizing_node = max(current.children, key=self.get_UCB1)
                current = maximizing_node
                
            if current.visits > 0 and not current.board.is_terminal():
                children = set([Node(s, current) for s in current.board.get_states()])
                current.children.update(children)
                current = random.choice(list(current.children))
            
            value = self.rollout(current)
            
            self.backpropagate(current, value)
            
                
    def rollout(self, node: Node) -> float:
        board = node.board
        
        while not board.is_terminal():
            board = random.choice(board.get_states())
        
        return board.get_score()
    
    def backpropagate(self, node: Node, value: float) -> None:
        while node is not None:
            node.score += value
            node.visits += 1
            node = node.parent
            