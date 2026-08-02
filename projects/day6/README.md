# Day 6: Damien Hirst Style Spot Painting Generator

A Python project that uses the `turtle` graphics library to generate a spot painting in the style of Damien Hirst's famous spin and spot paintings. The program extracts colour palettes directly from a reference image to paint a grid of randomized dots.

Additionally, this repository contains a structured, object-oriented playground demonstrating various turtle graphics techniques (dashed lines, shapes, random walks, and spirographs).

---

## Features

### 1. Spot Painting Generator (`src/main.py`)
*   **Colour Extraction:** Uses the `colorgram-py` package to analyze a reference image (`hirst_dots.png`) and extract a palette of dominant colours.
*   **Adaptive Background:** Dynamically detects the background colour of the reference image and sets the turtle window's background to match.
*   **Grid Layout:** Spawns a beautifully aligned 7x7 grid of coloured dots, choosing randomly from the extracted palette.
*   **Visual Preview:** Displays the source image and colour palette using `matplotlib` before starting the painting.

### 2. Turtle Playground (`src/painting_with_turtle.py`)
A class-based (`Paint`) environment showcasing intermediate turtle graphics capabilities:
*   **Multi-sided Shape Generator:** Draws polygons (from triangles up to 20-sided shapes) with randomized coluors.
*   **Random Walk:** Generates a randomized path with options for cardinal-only movements (0, 90, 180, 270 degrees) and varying segment lengths.
*   **Dashed Lines:** Custom logic to draw dashed lines.
*   **Spirograph:** Draws overlapping circles at offset angles to generate beautiful spirographs with random RGB colours. Includes error-handling for graceful shutdowns when closing the window mid-animation.

---

## File Structure

```text
day6/
├── pyproject.toml        # Project configuration & dependencies
├── README.md             # This file
├── uv.lock               # Lockfile for reproducible builds
└── src/
    ├── hirst_dots.png    # Reference image for Hirst's colour palette
    ├── main.py           # The Hirst Spot Painting application
    └── painting_with_turtle.py  # OOP Turtle graphics playground
```

---

## Installation

This project is managed with [uv](https://github.com/astral-sh/uv), an extremely fast Python package installer and resolver.

1.  Clone the repository and navigate to the project directory:
    ```bash
    cd projects/day6
    ```

2.  Install the required dependencies and set up the virtual environment:
    ```bash
    uv sync
    ```

---

## Usage

Ensure you are in the project's virtual environment before running the scripts.

### Generate the Spot Painting
To run the Damien Hirst style spot painting generator:
```bash
uv run src/main.py
```
This will:
1.  Open a `matplotlib` window showing the reference image. Close it to proceed.
2.  Open the turtle window and paint the grid. Click anywhere on the window to exit.

### Run the Turtle Playground
To explore other turtle drawing exercises (shapes, random walks, and the spirograph):
```bash
uv run src/painting_with_turtle.py
```
*Note: You can uncomment different sections at the bottom of `src/painting_with_turtle.py` to toggle between the shape generator, random walk, or spirograph.*
