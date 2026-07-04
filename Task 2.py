import math
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def is_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def minimax(board, depth, is_max):
    winner = check_winner(board)

    if winner == "O":
        return 1

    if winner == "X":
        return -1

    if is_full(board):
        return 0

    if is_max:
        best_score = -math.inf

        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)

        return best_score

    else:
        best_score = math.inf

        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)

        return best_score

def ai_move(board):
    best_score = -math.inf
    move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"

                score = minimax(board, 0, False)

                board[i][j] = " "

                if score > best_score:
                    best_score = score
                    move = (i, j)

    board[move[0]][move[1]] = "O"

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]

    print("TIC-TAC-TOE")
    print("You = X")
    print("AI = O")

    while True:
        print_board(board)
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))

        if board[row][col] != " ":
            print("Invalid Move!")
            continue

        board[row][col] = "X"

        if check_winner(board) == "X":
            print_board(board)
            print("You Win!")
            break

        if is_full(board):
            print_board(board)
            print("Draw!")
            break

        ai_move(board)

        if check_winner(board) == "O":
            print_board(board)
            print("AI Wins!")
            break

        if is_full(board):
            print_board(board)
            print("Draw!")
            break
play_game()

