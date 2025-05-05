def validate_move(board, move):
    return 0 <= move < 9 and board.board[move] == ' '

def get_available_moves(board):
    return (i for i, v in enumerate(board.board) if v == ' ')
