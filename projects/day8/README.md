# Day 8: Classic Snake Game

A recreation of the classic arcade game "Snake," built with Python's `turtle` library. The player controls a snake that grows longer by eating food while avoiding collisions with the screen boundaries and its own body.

---

## Features

*   **Classic Gameplay:** A faithful implementation of the beloved snake game mechanic.
*   **Interactive Difficulty:** Before starting, the player can choose between Easy, Medium, and Hard modes, which control the snake's speed.
*   **Responsive Controls:** The snake is controlled using the `W` (up), `A` (left), `S` (down), and `D` (right) keys. The game queues the next move to ensure fluid turns without allowing the snake to reverse directly into itself.
*   **Dynamic Growth:** The snake grows by one segment each time it consumes a piece of food.
*   **Collision Detection:** The game ends if the snake collides with any of the four screen boundaries or if it runs into its own body.
*   **Scoring System:** The final score is displayed at the end of the game, tracking how many pieces of food were eaten.

---

## File Structure

```text
day8/
├── pyproject.toml        # Project configuration
├── README.md             # This file
└── src/
    ├── main.py           # Main application logic and game loop
    └── snake_controls.py # Functions for snake movement, food, and game state
```

---

## Installation

This project is managed with [uv](https://github.com/astral-sh/uv).

1.  Navigate to the project directory:
    ```bash
    cd projects/day8
    ```

2.  Set up the virtual environment (if you haven't already):
    ```bash
    uv venv
    ```
    *Note: Since there are no external dependencies, `uv sync` is not required.*

---

## Usage

To run the Snake game, execute the main script from the project root:
```bash
uv run src/main.py
```
