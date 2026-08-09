# Day 10: Beach Dash

A classic "frogger" style game where the player must guide a baby turtle across a beach full of scuttling crabs to the safety of the sea. Built with Python's `turtle` library.

---

## Features

*   **Classic Frogger Gameplay:** Guide a baby turtle from its nest at the bottom of the screen to the ocean at the top.
*   **Dynamic Obstacles:** Dodge the crabs that move horizontally across the screen. Crabs spawn from either side at random intervals.
*   **Progressive Difficulty:** As the player successfully reaches the sea, the level increases, and more crabs will spawn, making the crossing more challenging.
*   **Responsive Controls:** The turtle is controlled using the `W` (forwards), `S` (backwards), `A` (left), and `D` (right) keys.
*   **Collision Detection:** The game ends if the turtle is touched by a crab.
*   **Scoring System:** The score and difficulty increases each time the turtle successfully reaches the water. The final score is displayed at the end of the game.

---

## File Structure

The project is organised into several modules, each handling a specific part of the game logic in an object-oriented manner.

```text
day10_beach_dash/
├── pyproject.toml        # Project configuration
├── README.md             # This file
└── src/
    ├── main.py           # Main game loop and application entry point
    ├── baby_turtles.py   # Defines the player-controlled BabyTurtle class
    ├── crabs.py          # Defines the Crab enemy class and its movement
    ├── scoreboard.py     # Manages and displays the game score
    ├── background.py     # Draws the static background scene (sea, beach)
    └── beach_rows.py     # Defines the invisible 'lanes' for crab spawning
```

---

## Installation

This project is managed with [uv](https://github.com/astral-sh/uv).

1.  Navigate to the project directory:
    ```bash
    cd projects/day10_beach_dash
    ```

2.  Set up the virtual environment (if you haven't already):
    ```bash
    uv venv
    ```
    *Note: Since there are no external dependencies, `uv sync` is not required.*

---

## Usage

To run the game, execute the `main.py` script from the project root:
```bash
uv run src/main.py
```
