# Day 16: PassMan - Desktop Password Manager

A lightweight, local-first Desktop Password Manager built with Python and Tkinter. This application offers a clean graphical interface to securely store and generate complex passwords for various websites, keeping credentials saved locally on your machine in a structured format.

---

## 🚀 Features

- **Graphical User Interface (GUI):** Built with Python's standard `tkinter` library, featuring custom alignments, entry validation, dynamic feedback labels, and custom logo styling.
- **Random Password Generator:** Generates a strong, random 15-character alphanumeric password with a single click.
- **Clipboard Integration:** Generated passwords are automatically copied to your system clipboard (using `pyperclip`) for a seamless, copy-paste-ready user experience.
- **Local JSON Storage:** Saves credential details (website URL, username/email, password) in a local JSON database. It automatically reads and merges with existing credentials.
- **Form Validation:** Validates form inputs, displaying instant status messages (e.g., "Saved!", "Missing URL", "Missing username") to prevent incomplete credentials from being saved.
- **Security-First Local Design:** Your sensitive database file is ignored by Git (`data/.gitignore`) to prevent accidental commits of passwords to public repositories.

---

## 🛠️ Skills & Technologies Practiced

- **GUI Development (Tkinter):** Layout management using the `grid` system (`columnspan`, `sticky` alignments), canvas rendering for images (`PhotoImage`), widget focus control (`focus()`), and state tracking using `StringVar` and configuration updates.
- **File I/O & Serialization (JSON):** Dynamic JSON file reading (`json.load`), safe appending/updating (`dict.update`), and writing/truncating files (`json.dump`, `f.seek(0)`, `f.truncate()`).
- **Clipboard Control:** Copying text to the OS clipboard programmatically using `pyperclip`.
- **Credential Protection:** Utilizing local ignore rules (`.gitignore`) specifically for data-store outputs.

---

## 📂 Project Structure

```text
day16_password_manager/
├── pyproject.toml       # Python project metadata and dependencies (pyperclip)
├── README.md            # Project documentation (this file)
├── uv.lock              # Lockfile for precise dependency resolution
├── data/
│   ├── .gitignore       # Directs git to ignore saved_details.json
│   ├── logo.png         # PassMan application logo
│   └── saved_details.json # Local credentials storage (generated at first save, git-ignored)
└── src/
    ├── main.py          # Tkinter UI construction and event handling loop
    └── passman_funcs.py # Business logic: random generation and JSON saving
```

---

## ⚙️ How to Run

This project uses [`uv`](https://github.com/astral-sh/uv) for fast, modern dependency and virtual environment management.

### Prerequisites

Make sure you have Python 3.12+ and `uv` installed. If you don't have `uv`, install it via curl or your package manager:
```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Running the Application

To run the password manager in its virtual environment, run:

```bash
uv run src/main.py
```

*Note: On some systems (such as macOS/Linux), Tkinter requires system-level packages (e.g., `brew install python-tk` or `sudo apt-get install python3-tk`).*

---

## 🔒 Security Note

- All credential records are stored in `data/saved_details.json`.
- This file is strictly ignored by Git via the rule in `data/.gitignore`:
  ```text
  saved_details.*
  ```
- **Never** remove this ignore rule or commit your `saved_details.json` to GitHub or any public remote repositories.
