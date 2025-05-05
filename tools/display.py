def show_welcome():
    print("Welcome to Tic-Tac-Toe!")

def show_board(board):
    b = board.board
    print(f"{b[0]} | {b[1]} | {b[2]}\n---------")
    print(f"{b[3]} | {b[4]} | {b[5]}\n---------")
    print(f"{b[6]} | {b[7]} | {b[8]}")

def show_winner(name):
    print(f"\n{name} wins the game!")
