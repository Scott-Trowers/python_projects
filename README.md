# 100 days of code

Small Python projects, one per day, to build consistent practice and improve Python fluency.

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

The script at the repo root — run it from the repo root, passing the day number:

```bash
./new_day.sh 17
```

This creates `projects/day17/` with a uv project initialised and `src/main.py` ready to go.

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
