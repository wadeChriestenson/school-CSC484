import numpy as np

def print_board(board):
    print()
    print(board)
    print()

def check_winner(board, player):
    for row in board:
        if np.all(row == player):
            return True

    for col in board.T:
        if np.all(col == player):
            return True

    if np.all(np.diag(board) == player):
        return True

    if np.all(np.diag(np.fliplr(board)) == player):
        return True

    return False

def check_draw(board):
    return not np.any(board == " ")

board = np.full((3, 3), " ")
players = ["X", "O"]
turn = 0

while True:
    print_board(board)
    player = players[turn % 2]

    print(f"Player {player}'s turn")

    row = int(input("Enter row index 0, 1, or 2: "))
    col = int(input("Enter column index 0, 1, or 2: "))

    if row < 0 or row > 2 or col < 0 or col > 2:
        print("Invalid move. Row and column must be between 0 and 2.")
        continue

    if board[row, col] != " ":
        print("That square is already taken. Try again.")
        continue

    board[row, col] = player

    if check_winner(board, player):
        print_board(board)
        print(f"Player {player} wins!")
        break

    if check_draw(board):
        print_board(board)
        print("The game is a draw!")
        break

    turn += 1