from collections import deque
import time

N = 14
# ===================================================================================
# Game logic 
# ===================================================================================

def create_start_state(n: int) -> str:
    return '>' * n + ' ' + '<' * n


def create_target_state(n: int) -> str:
    return '<' * n + ' ' + '>' * n


def make_short_move_if_possible(state: str, i: int) -> str:
    if i >= len(state) or i < 0:
        raise ValueError('Index out of bound')
    if (state[i] == '>' and i + 1 >= len(state)) or (state[i] == '<' and i < 1):
        return state

    if state[i] == '>' and state[i + 1] == ' ':
        state = state[:i] + ' >' + state[i + 2:]
    if state[i] == '<' and state[i - 1] == ' ':
        state = state[:i - 1] + '< ' + state[i + 1:]
        
    return state


def make_long_move_if_possible(state: str, i: int) -> str:
    if i >= len(state) or i < 0:
        raise ValueError('Index out of bound')
    if (state[i] == '>' and i + 2 >= len(state)) or (state[i] == '<' and i < 2):
        return state
    
    if state[i] == '>' and state[i + 2] == ' ':
        state = state[:i] + ' ' + state[i + 1] + '>' + state[i + 3:]
        
    if state[i] == '<' and state[i - 2] == ' ':
        state = state[:i - 2] + '<' + state[i - 1] + ' ' + state[i + 1:]
        
    return state

# ===================================================================================
# Search logic 
# ===================================================================================

def generate_all_states(state: str) -> list[str]:
    result = []
    
    for i in range(len(state)):
        s = make_short_move_if_possible(state, i)
        l = make_long_move_if_possible(state, i)
        
        if s != state:
            result.append(s)
        if l != state:
            result.append(l)
        
    return result

def dfs(root: str) -> tuple[bool, dict, str]:
    tree = dict()
    depth = 1000
    
    found, remaining = dfs_rec(root, tree, 1000000)
    # while True:
    #     found, remaining = dfs_rec(root, tree, depth)
    #     if found is not None:
    #         return True, tree, found
    #     elif not remaining:
    #         return False, tree, None
    #     depth += 1
    
    return True, tree, found
        

def dfs_rec(node: str, tree: dict, depth: int) -> tuple[str, bool]:
    if depth == 0:
        if node == create_target_state(N):
            return node, True
        else:
            return None, True
        
    elif depth > 0:
        any_remaining = False
        for child in generate_all_states(node):
            tree[child] = node
            found, remaining = dfs_rec(child, tree, depth - 1)
            if found != None:
                return found, True
            if remaining:
                any_remaining = True
        
        return None, any_remaining
    
# ===================================================================================
# Helper functions
# ===================================================================================

def generate_path_from_tree(tree: dict) -> list[str]:
    current = create_target_state(N)
    result = [current]
    
    while True:
        if current not in tree.keys():
            return list(reversed(result))
        else:
            current = tree[current]
            result.append(current)
        
        
def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time() 
        result = func(*args, **kwargs)  
        end_time = time.time()  
        execution_time = end_time - start_time  
        print(f"Function '{func.__name__}' executed in {execution_time:.6f} seconds")
        return result  
    return wrapper
        
        
@timeit
def solve() -> list[str]:
    start = create_start_state(N)
    found, tree, target = dfs(start)
    if found:
        result_path = generate_path_from_tree(tree)
        return result_path
    else:
        return []
    
    
def main() -> None: 
    result = solve()
    print(f'Result is: {result}')

if __name__ == '__main__':
    main()
    