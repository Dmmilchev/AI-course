from board import Board
from bot import Bot


def play_game():
    board = Board()
    bot = Bot(player=1)

    user_first = input("Do you want to play first? (yes/no): ").lower() == "yes"
    
    while not board.is_terminal() and board.get_empty_squares():
        if user_first:
            print("\nCurrent board:")
            print(board)

            while True:
                try:
                    move = input("Your move (row col): ")
                    row, col = map(int, move.split())

                    if (row, col) not in board.get_empty_squares():
                        print("Invalid move! That square is already taken or out of bounds. Try again.")
                        continue

                    board.make_move(-1, (row, col))
                    break
                except (ValueError, IndexError):
                    print("Invalid input! Please enter row and column numbers separated by a space.")

            if board.is_player_winning(-1):
                print("\nYou win!")
                print(board)
                return
            
            user_first = False

        else:
            bot_move = bot.get_best_move(board)
            board.make_move(1, bot_move)
            print("\nBot's move:")
            print(board)

            if board.is_player_winning(1):
                print("\nThe bot wins!")
                print(board)
                return
            
            user_first = True

    print("\nIt's a draw!")
    print(board)

if __name__ == '__main__':
    play_game()