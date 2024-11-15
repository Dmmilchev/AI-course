from board import Board
from bot import Bot

def play_game():
    board = Board()
    bot = Bot()
    
    print("Welcome to Tic Tac Toe!")
    print("You'll be playing as O, and the bot will be X")
    print("Enter your moves as row,column (1-3)")
    print("For example: '2,3' for middle row, right column")
    print("\nInitial board:")
    print(board)
    
    while not board.is_terminal():
        if board.turn == 1:  # Bot's turn (X)
            print("\nBot is thinking...")
            bot.get_best_move(board)
            # Choose the most visited child as the best move
            best_child = max(bot.root.children, key=lambda x: x.visits)
            board = best_child.board
            print("\nBot's move:")
            print(board)
            
        else:  # Player's turn (O)
            while True:
                try:
                    move = input("\nEnter your move (row,column): ")
                    row, col = map(int, move.strip().split(','))
                    
                    if (row, col) not in board.get_empty_squares():
                        print("That square is already taken! Try again.")
                        continue
                        
                    if not (1 <= row <= 3 and 1 <= col <= 3):
                        print("Invalid input! Row and column must be between 1 and 3.")
                        continue
                    
                    board._make_move((row, col))
                    print("\nYour move:")
                    print(board)
                    break
                    
                except (ValueError, IndexError):
                    print("Invalid input! Please use the format 'row,column' (e.g., '2,3')")
    # Game over - determine the result
    if board.is_player_winning(1):
        print("\nGame Over - Bot wins!")
    elif board.is_player_winning(-1):
        print("\nGame Over - You win!")
    else:
        print("\nGame Over - It's a draw!")

if __name__ == "__main__":
    play_game()