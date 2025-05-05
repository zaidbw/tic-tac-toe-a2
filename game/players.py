import random

class Player:
    def __init__(self, name, marker, is_computer=False):
        self.name = name
        self.marker = marker
        self.is_computer = is_computer

    def get_move(self, board):
        if self.is_computer:
            return random.choice([i for i, val in enumerate(board.board) if val == ' '])
        else:
            return int(input(f"{self.name}'s move (0-8): "))
