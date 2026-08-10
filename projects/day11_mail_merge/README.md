# Day 11: Mail Merge

A Python script that automates the creation of personalized letters using a template and a list of names.

---

## Features

*   **Template-Based:** Reads a base letter template from a file (`starting_letter.txt`).
*   **Dynamic Personalization:** Reads a list of recipient names from a separate file (`invited_names.txt`).
*   **Placeholder Replacement:** Dynamically replaces a `[name]` placeholder in the template with each recipient's name.
*   **Clean Output:** Strips newline characters from the input names to ensure clean formatting in the output letters.
*   **Automated File Creation:** Saves each personalized letter as a new `.txt` file in a designated output directory.
*   **Safe Execution:** The script is designed to prevent accidental overwrites. It will raise an error if the output files it tries to create already exist.

---

## File Structure

The project is organized into the main script and input/output directories.

```text
day11_mail_merge/
├── pyproject.toml        # Project configuration
├── README.md             # This file
└── src/
    ├── main.py           # Main script for the mail merge logic
    ├── Input/
    │   ├── Letters/
    │   │   └── starting_letter.txt   # The letter template
    │   └── Names/
    │       └── invited_names.txt     # List of recipient names
    └── Output/
        └── ReadyToSend/              # Directory for the generated letters
```

---

## Installation

This project is managed with [uv](https://github.com/astral-sh/uv).

1.  Navigate to the project directory:
    ```bash
    cd projects/day11_mail_merge
    ```

2.  Set up the virtual environment (if you haven't already):
    ```bash
    uv venv
    ```
    *Note: Since there are no external dependencies, `uv sync` is not required.*

---

## Usage

The script must be run from the `src` directory because it uses relative paths to locate the `Input` and `Output` folders.

1.  **Prepare for Execution:** Before running, ensure the `src/Output/ReadyToSend/` directory is empty. The script will error if the output files already exist.

2.  Navigate to the `src` directory:
    ```bash
    cd projects/day11_mail_merge/src
    ```

3.  Run the script using Python:
    ```bash
    python main.py
    ```
    The personalized letters will be generated and saved in the `src/Output/ReadyToSend/` directory.
