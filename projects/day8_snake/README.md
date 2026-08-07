# Day 8: Classic Snake Game

A recreation of the classic arcade game "Snake," built with Python's `turtle` library. The player controls a snake that grows longer by eating food while avoiding collisions with the screen boundaries and its own body.

This project includes two implementations: a modern object-oriented (OOP) version and a legacy procedural version.

---

## Features

*   **Classic Gameplay:** A faithful implementation of the beloved snake game mechanic.
*   **Interactive Difficulty:** Before starting, the player can choose between Easy, Medium, and Hard modes, which control the snake's speed.
*   **Responsive Controls:** The snake is controlled using the `W` (up), `A` (left), `S` (down), and `D` (right) keys. The game queues the next move to ensure fluid turns without allowing the snake to reverse directly into itself.
*   **Dynamic Growth:** The snake grows by one segment each time it consumes a piece of food.
*   **Collision Detection:** The game ends if the snake collides with any of the four screen boundaries or if it runs into its own body.
*   **Scoring System:** The final score is displayed at the end of the game, tracking how many pieces of food were eaten.

---

## Implementations

### Object-Oriented Version (Recommended)

The main logic has been refactored into a fully object-oriented script, `snake.py`. This version encapsulates the game's components—the snake, the food, the screen (`SnakePit`), and the game controller (`SnakeCharmer`)—into distinct classes. This approach improves modularity, readability, and makes the code easier to maintain and extend.

This is the recommended version to run.

### Semi-Procedural Version (Legacy)

The original version of the game was built using a procedural approach. The files for this version are located in the `src/semi-procedural` directory.

**Note:** This version is considered legacy and is no longer actively maintained. The `snake_controls.py` file has been refactored, and its functions are largely commented out, so this version is not functional in its current state. It remains in the repository for historical and educational purposes to show the evolution of the codebase.

---

## File Structure

```text
day8/
├── pyproject.toml        # Project configuration
├── README.md             # This file
└── src/
    ├── snake.py          # Recommended: Standalone object-oriented version of the game
    └── semi-procedural/
        ├── main.py           # Legacy: Main application logic for the procedural version
        └── snake_controls.py # Legacy: Helper functions for the procedural version
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

To run the recommended object-oriented Snake game, execute the `snake.py` script from the project root:
```bash
uv run src/snake.py
```
To attempt to run the legacy semi-procedural version:
```bash
uv run src/semi-procedural/main.py
```
*(Note: As mentioned, the legacy version is not currently functional.)*
