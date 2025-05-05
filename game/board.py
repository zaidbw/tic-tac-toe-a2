class Board:
    def __init__(self):
        self.board = [' ' for _ in range(9)]

    def place_move(self, position, marker):
        self.board[position] = marker

    def is_draw(self):
        return ' ' not in self.board

    def check_win(self, marker):
        win_conditions = [
            [0,1,2], [3,4,5], [6,7,8],  # Rows
            [0,3,6], [1,4,7], [2,5,8],  # Columns
            [0,4,8], [2,4,6]            # Diagonals
        ]
        return any(all(self.board[i] == marker for i in combo) for combo in win_conditions)
