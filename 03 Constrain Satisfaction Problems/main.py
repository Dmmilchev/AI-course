from board import Board

import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Start time
        result = func(*args, **kwargs)  # Execute the function
        end_time = time.time()  # End time
        elapsed_time = end_time - start_time  # Calculate elapsed time
        print(f"Function '{func.__name__}' took {elapsed_time:.4f} seconds to execute.")
        return result
    return wrapper

@time_it
def solve(N):
    board = Board(N)
    while  True:
        max, col = board.get_column_with_max_conflicts()
        if max == 0:
            return board
        row = board.get_row_with_min_conflicts(col)
        board.remove_queen_on_col(col)
        board.put_queen_on_coord((row, col))
    
def main() -> None:
    # board = Board2(4)
    # board.put_queen_on_coord((1,1))
    # board.put_queen_on_coord((2, 2))
    # print(board.get_row_with_min_conflicts(5))
    # print(str(board))
    board = solve(3000)
    #print(str(board))
    
if __name__ == '__main__':
    main()
    