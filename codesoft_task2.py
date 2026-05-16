@ -0,0 +1,82 @@

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    current_player = "X"

    print("=== TIC TAC TOE GAME ===")
    print("Player X and Player O")
    print("Enter row and column numbers from 1 to 3")

    while True:

        print_board(board)

        try:
            row = int(input(f"Player {current_player} - Enter row (1-3): ")) - 1
            col = int(input(f"Player {current_player} - Enter column (1-3): ")) - 1

            if row not in range(3) or col not in range(3):
                print("Invalid position! Try again.")
                continue

            if board[row][col] != " ":
                print("Position already taken! Try again.")
                continue
            board[row][col] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"🎉 Player {current_player} wins!")
                break

         
            if check_draw(board):
                print_board(board)
                print("🤝 It's a draw!")
                break

            
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"

        except ValueError:
            print("Please enter valid numbers!")



tic_tac_toe()
