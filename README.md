# 100 days of code

Small Python projects, one per day, to build consistent practice and improve Python fluency. Code is written without AI assistance; AI is used for documentation only.

Each project lives in `projects/dayN/` as an independent uv-managed Python project.

## Structure

```
projects/
  day16/
    src/
      main.py
    pyproject.toml
    .python-version
    .gitignore
  day17/
    ...
```

## Starting a new project

The script at the repo root — run it from the repo root, passing the day number.

To automatically navigate your terminal into the newly created directory, run the script with `source` (or `.`):

```bash
source ./new_day.sh 17
```

Alternatively, you can run it directly, though your terminal won't navigate automatically:

```bash
./new_day.sh 17
```

This creates `projects/day17/`, initializes a self-contained uv project, moves `main.py` into `src/`, and runs `uv sync`.

### Manual steps (for reference)

1. Create a folder for the day and move into it:

   ```bash
   mkdir projects/dayN && cd projects/dayN
   ```

2. Initialise a uv project (the `--no-workspace` flag keeps it self-contained):

   ```bash
   uv init --no-workspace
   ```

3. Move the generated `main.py` into `src/`:

   ```bash
   mkdir src && mv main.py src/main.py
   ```

4. Add any dependencies:

   ```bash
   uv add pandas
   ```

5. Run the script:

   ```bash
   uv run src/main.py
   ```

uv handles the virtual environment automatically — no need to activate it manually.
