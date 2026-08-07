# Day 9: Classic Pong Game

A recreation of the classic arcade game "Pong," built with Python's `turtle` library using an object-oriented approach. The game features two paddles controlled by the players, a ball that bounces off walls and paddles, and a scoring system.

---

## Features

*   **Classic Gameplay:** A faithful implementation of the iconic Pong game mechanic.
*   **Two-Player Action:** Player 1 uses the `W` and `S` keys, and Player 2 uses the `Up` and `Down` arrow keys to control their paddles.
*   **Dynamic Ball Physics:** The ball bounces realistically off the top and bottom walls and the paddles.
*   **Scoring System:** The game keeps track of the score for each player. A point is awarded when the opponent fails to return the ball.
*   **Game End Condition:** The game ends when one of the players reaches a predefined score.
*   **Object-Oriented Design:** The game is structured using classes for the paddles, ball, and scoreboard, promoting modularity and readability.

---

## File Structure

```text
day9/
├── pyproject.toml        # Project configuration
├── README.md             # This file
└── src/
    ├── main.py           # Main application logic and game loop
    ├── paddles.py        # Defines the PongPaddle class
    ├── pong_ball.py      # Defines the PongBall class
    ├── pong_court.py     # (Currently unused) Intended for drawing court markings
    └── scoreboard.py     # Defines the ScoreBoard class
```

---

## Requirements

This project uses the `turtle` graphics library, which is part of the Python standard library. No external packages are required.

---

## Installation

This project is managed with [uv](https://github.com/astral-sh/uv).

1.  Navigate to the project directory:
    ```bash
    cd projects/day9
    ```

2.  Set up the virtual environment (if you haven't already):
    ```bash
    uv venv
    ```
    *Note: Since there are no external dependencies, `uv sync` is not required.*

---

## Usage

To run the Pong game, execute the `main.py` script from the project root:
```bash
uv run src/main.py
```
