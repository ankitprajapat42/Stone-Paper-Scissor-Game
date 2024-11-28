# Stone-Paper-Scissor Game

This is a simple console-based **Stone-Paper-Scissor Game** implemented in Python. The game allows the user to play against the computer, where both players choose one of the three options: Stone, Paper, or Scissor. The winner is determined based on the standard game rules:

- **Stone beats Scissor** (Stone crushes Scissor)
- **Scissor beats Paper** (Scissor cuts Paper)
- **Paper beats Stone** (Paper wraps Stone)

## Features
- Interactive console-based gameplay.
- Option to play multiple rounds until the user decides to exit.
- Randomized computer choices using `numpy` for fairness.
- Input validation to handle invalid choices.

## How to Play
1. Run the script in any Python environment.
2. Enter your choice:
   - `1` for Stone
   - `2` for Paper
   - `3` for Scissor
3. The computer will randomly select its choice.
4. The game will display the result of the round:
   - **Win**, **Loss**, or **Draw**.
5. After each round, choose whether to play again or exit.

## Requirements
- Python 3.x
- `numpy` library

Install `numpy` using:
```bash
pip install numpy
