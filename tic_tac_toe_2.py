import random

# ---------------------------
# 1. Board setup and display
# ---------------------------
def create_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def display_board(board):
    pos = 1
    for i in range(3):
        row = ""
        for j in range(3):
            row += board[i][j] if board[i][j] != ' ' else str(pos)
            if j < 2:
                row += " | "
            pos += 1
        print(row)
        if i < 2:
            print("---------")
    print()

# ---------------------------
# 2. Player move
# ---------------------------
def player_move(board):
    while True:
        try:
            choice = int(input("Choose your spot (1-9): "))
            if 1 <= choice <= 9:
                row = (choice - 1) // 3
                col = (choice - 1) % 3
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    break
                else:
                    print("Spot taken. Try again.")
            else:
                print("Invalid number. Pick 1-9.")
        except ValueError:
            print("Enter a valid integer 1-9.")

# ---------------------------
# 3. Check for winner
# ---------------------------
def check_winner(board, symbol):
    for i in range(3):
        if all(board[i][j] == symbol for j in range(3)):
            return True
        if all(board[j][i] == symbol for j in range(3)):
            return True
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return True
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        return True
    return False

# ---------------------------
# 4. Computer move
# ---------------------------
def computer_move(board):
    def simulate(symbol):
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = symbol
                    if check_winner(board, symbol):
                        board[i][j] = ' '
                        return i, j
                    board[i][j] = ' '
        return None

    move = simulate('O')
    if move:
        board[move[0]][move[1]] = 'O'
        return

    move = simulate('X')
    if move:
        board[move[0]][move[1]] = 'O'
        return

    empty = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    move = random.choice(empty)
    board[move[0]][move[1]] = 'O'

# ---------------------------
# 5. Check for tie
# ---------------------------
def is_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

# ---------------------------
# 6. Game loop
# ---------------------------
def play_game():
    board = create_board()
    # BONUS: randomly decide who starts
    player_turn = random.choice([True, False])
    if player_turn:
        print("You go first (X)!")
    else:
        print("Computer goes first (O)!")

    while True:
        display_board(board)
        if player_turn:
            player_move(board)
            if check_winner(board, 'X'):
                display_board(board)
                print("You win!")
                return 'X'
        else:
            computer_move(board)
            if check_winner(board, 'O'):
                display_board(board)
                print("Computer wins!")
                return 'O'
        if is_full(board):
            display_board(board)
            print("It's a tie!")
            return 'Tie'
        player_turn = not player_turn

# ---------------------------
# 7. Main program with replay
# ---------------------------
score = {'X': 0, 'O': 0, 'Tie': 0}

while True:
    winner = play_game()
    score[winner] += 1
    print(f"Score -> You: {score['X']}, Computer: {score['O']}, Ties: {score['Tie']}")
    again = input("Play again? (y/n): ").lower()
    if again != 'y':
        print("Thanks for playing!")
        break
