from puzzle import Puzzle
import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time() 
        result = func(*args, **kwargs)  
        end_time = time.time()  
        execution_time = end_time - start_time  
        print(f"Function '{func.__name__}' executed in {execution_time:.2f} seconds")
        return result  
    return wrapper


@timeit
def start_ida_star(puzzle: Puzzle):
    if not puzzle.is_solvable():
        raise ValueError('Puzzle not solvable')
    
    if puzzle.is_goal():
        return [], []
    
    bound = puzzle.h()
    path = set([puzzle])
    transitions = []
    
    while True:
        remaining = search(puzzle, path, 0, bound, transitions)
        if remaining == True:
            return path, transitions
        bound = remaining
        
        
def search(node: Puzzle, path: set[Puzzle], g, bound, moves):
    f = g + node.h()
    
    if f > bound:
        return f
  
    if node.is_goal():
        return True 
     
    min = float('inf')
    
    children = []
    for move in Puzzle.MOVES:
        isValid, nextNode = node.try_move(move)
        if isValid:
            children.append((nextNode, move))
    children = sorted(children, key=lambda x: x[0].h())
        
    for nextNode, move in children:
        if moves and (-move[0], -move[1]) == moves[-1]:
            continue
        if nextNode in path:
            continue
        
        path.add(nextNode)
        moves.append(move)
        
        t = search(nextNode, path, g + 1, bound, moves)
        
        if t == True:
            return True
        if t < min:
            min = t
            
        path.remove(nextNode)
        moves.pop()
        
    return min

