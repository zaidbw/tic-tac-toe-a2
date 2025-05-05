from pathlib import Path

class Logger:
    def __init__(self):
        self.game_dir = self._create_game_folder()
        self.log_file = self.game_dir / "log.txt"
        self.log_file.touch()

    def _create_game_folder(self):
        base = Path("game_log")
        base.mkdir(exist_ok=True)
        existing = list(base.glob("game*/"))
        next_num = len(existing) + 1
        game_folder = base / f"game{next_num}"
        game_folder.mkdir(parents=True, exist_ok=True)
        return game_folder

    def log_move(self, move_num, player, position, board):
        with self.log_file.open("a") as f:
            f.write(f"Move {move_num}: {player} -> {position}\n")
            f.write(self._board_to_string(board) + "\n\n")

    def log_result(self, result):
        with self.log_file.open("a") as f:
            f.write(f"Game Result: {result}\n")

    def _board_to_string(self, board):
        b = board.board
        return f"{b[0]} | {b[1]} | {b[2]}\n---------\n{b[3]} | {b[4]} | {b[5]}\n---------\n{b[6]} | {b[7]} | {b[8]}"
