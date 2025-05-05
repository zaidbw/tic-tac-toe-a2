# Tic-Tac-Toe Command Line Game

This is a simple command-line Tic-Tac-Toe game built using Python. The game allows two players to take turns, making moves on a 3x3 board. It includes logging of each move and game history.

## Project Structure

- `main.py`: The main file that runs the game.
- `game/`: Contains the core game logic, including board management and player functionality.
  - `board.py`: Manages the board state and checks for winning conditions.
  - `players.py`: Defines the player class and handles player input.
  - `utils.py`: Provides utility functions for validating moves and other game operations.
- `tools/`: Contains helper modules for displaying the game and logging moves.
  - `display.py`: Handles all display-related functions.
  - `logger.py`: Logs each move and game result to a file.

## How to **Run** the Game

1. Clone the repository
   ```bash
   git clone https://github.com/your-username/tic-tac-toe-a2.git
2. Navigate to the project folder
```bash
cd tic-tac-toe-a2
```
3. Run the game
```bash
python main.py
```
## How to **Play** the Game

1. **Start the Game**: After running the game (`python main.py`), you will be prompted to enter player names.

2. **Choose Game Mode**:
   - **Player vs Player**: Both players take turns to place their markers (X or O).
   - **Player vs Computer**: One player takes turns with the computer, which makes random moves.

3. **Make a Move**: The game will ask each player to enter their move (row and column) for placing their marker.

4. **Winning the Game**: The first player to get three markers in a row (horizontally, vertically, or diagonally) wins the game.

5. **Game End**: If all spaces are filled and no one wins, the game ends in a draw.

6. **Replay Option**: After each game, you can choose to start a new game or exit.


