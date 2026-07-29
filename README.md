# 100 days of code

100 small Python projects, one per day, to build consistent practice and improve Python fluency.

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

1. Create a folder for the day and move into it:

   ```bash
   mkdir projects/dayN && cd projects/dayN
   ```

2. Initialise a uv project (the `--no-workspace` flag keeps it self-contained):

   ```bash
   uv init --no-workspace
   ```

   This creates `pyproject.toml`, `main.py`, `.python-version`, and `.gitignore`.

3. Add any dependencies you need:

   ```bash
   uv add requests
   ```

4. Run the script:

   ```bash
   uv run main.py
   ```

That's it — uv handles the virtual environment automatically. No need to activate anything manually.
