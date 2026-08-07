# Day 7: Turtle Race & Etch-a-Sketch

A project showcasing two interactive applications built with Python's `turtle` library: a turtle racing game and a free-form Etch-a-Sketch style drawing program.

---

## Features

### 1. Turtle Race Game (`src/main.py`)
A simulation of a classic racing game where users bet on one of four contestants.
*   **Interactive Betting:** Prompts the user to predict the winner from four named turtles (Leo, Raphael, Donatello, Michelangelo).
*   **Randomized Race:** Each turtle advances at a random speed in every turn, making each race unpredictable.
*   **Dynamic Finishers:** The program tracks the exact order that all turtles cross the finish line.
*   **Podium Celebration:** After the race, the top three turtles are displayed on a winner's podium.
*   **Win/Lose Outcome:** A final message announces the winning turtle and declares whether the user's prediction was correct.

### 2. Etch-a-Sketch (`src/turtle_drawer.py`)
A free-form drawing application controlled entirely by keyboard inputs.
*   **Keyboard Control:** Uses continuous key presses to control the turtle's movement and drawing actions, creating a smooth drawing experience.
*   **Movement:** Use `a` and `d` for forward/backward movement, and the `Left` and `Right` arrow keys for turning.
*   **Pen Control:** The `space` bar toggles the turtle's pen up and down, allowing you to move without drawing.
*   **Clear Screen:** The `c` key clears the entire drawing and resets the turtle to the center of the screen.

---

## File Structure

```text
day7/
├── pyproject.toml        # Project configuration
├── README.md             # This file
└── src/
    ├── main.py           # The Turtle Race game application
    └── turtle_drawer.py  # The Etch-a-Sketch drawing application
```

---

## Installation

This project is managed with [uv](https://github.com/astral-sh/uv).

1.  Navigate to the project directory:
    ```bash
    cd projects/day7
    ```

2.  Set up the virtual environment (if you haven't already):
    ```bash
    uv venv
    ```
    *Note: Since there are no external dependencies, `uv sync` is not required.*

---

## Usage

### Run the Turtle Race Game
```bash
uv run src/main.py
```

### Run the Etch-a-Sketch
```bash
uv run src/turtle_drawer.py
```
