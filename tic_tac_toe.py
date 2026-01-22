# 1. Create a 3x3 board and populate with spaces
board = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(' ')
    board.append(row)

# 2. Function to display the board neatly
def display_board(board):
    position = 1
    for i in range(3):
        row_display = ""
        for j in range(3):
            if board[i][j] == ' ':
                row_display += str(position)
            else:
                row_display += board[i][j]
            if j < 2:
                row_display += " | "
            position += 1
        print(row_display)
        if i < 2:
            print("---------")

# 3. Function to make a move
def make_move(board, symbol):
    while True:
        try:
            choice = int(input(f"Player {symbol}, choose a spot (1-9): "))
            if 1 <= choice <= 9:
                row = (choice - 1) // 3
                col = (choice - 1) % 3
                if board[row][col] == ' ':
                    board[row][col] = symbol
                    break
                else:
                    print("That spot is already taken. Try again.")
            else:
                print("Invalid choice. Pick a number from 1 to 9.")
        except ValueError:
            print("Invalid input. Enter an integer from 1 to 9.")

display_board(board)        # show empty board
make_move(board, 'X')       # player X moves
display_board(board)        # show board after move
make_move(board, 'O')       # player O moves
display_board(board)        # show board after move
