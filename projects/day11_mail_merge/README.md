# day 11 - mail merge

A Python script that automates the creation of personalized letters using a template and a list of names.

## how to run

```bash
uv run src/main.py
```

## skills

- file system I/O (reading templates and writing output files)
- string manipulation (stripping newlines, replacing placeholders)
- defensive programming (using 'x' write mode to prevent accidental overwrites)

## features

- reads a base letter template from a starting letter file
- reads and processes a list of recipient names
- dynamically replaces a `[name]` placeholder with each clean recipient name
- automatically saves each personalized letter to a designated output directory
