from game.board import Board
from game.players import Player
from game.utils import validate_move, get_available_moves
from tools.display import show_welcome, show_board, show_winner
from tools.logger import Logger

def main():
    show_welcome()

    name1 = input("Enter Player 1 name: ")
    name2 = input("Enter Player 2 name (or type 'Computer'): ")

    player1 = Player(name1, 'X')
    player2 = Player(name2, 'O', is_computer=(name2.lower() == 'computer'))

    board = Board()
    logger = Logger()

    current_player = player1
    move_number = 1

    while True:
        show_board(board)
        move = current_player.get_move(board)

        while not validate_move(board, move):
            print("Invalid move. Try again.")
            move = current_player.get_move(board)

        board.place_move(move, current_player.marker)
        logger.log_move(move_number, current_player.name, move, board)

        if board.check_win(current_player.marker):
            show_board(board)
            show_winner(current_player.name)
            logger.log_result(f"{current_player.name} wins")
            break

        if board.is_draw():
            show_board(board)
            print("It's a draw!")
            logger.log_result("Draw")
            break

        current_player = player2 if current_player == player1 else player1
        move_number += 1

    again = input("Play again? (y/n): ")
    if again.lower() == 'y':
        main()

if __name__ == "__main__":
    main()
