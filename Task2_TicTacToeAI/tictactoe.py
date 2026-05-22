board = [" " for x in range(9)]

def print_board():
    print()
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])
    print()

def check_winner(player):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    for combo in wins:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def ai_move():
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            return

print("Tic Tac Toe Game")

while True:
    print_board()

    move = int(input("Enter position (1-9): ")) - 1

    if board[move] == " ":
        board[move] = "X"
    else:
        print("Position already used")
        continue

    if check_winner("X"):
        print_board()
        print("You win!")
        break

    ai_move()

    if check_winner("O"):
        print_board()
        print("AI wins!")
        break
