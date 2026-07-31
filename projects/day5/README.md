# day 5 - quiz game (OOP)

A CLI-based trivia quiz game built from scratch using object-oriented programming.

## how to run

```bash
uv run src/main.py
```

## skills

- object-oriented programming — creating custom classes from scratch
- class state management and encapsulation
- robust input validation and formatting
- modular structure across multiple files

## classes

- `Question` — models a single quiz question, handles console prompt validation, and checks answers
- `QuizBrain` — manages quiz flow, instantiates questions, and tracks user scores and percentage metrics

## features

- interactive True/False questions sourced from a modular dataset
- input validation loops to ensure user inputs are strictly 'true' or 'false' (case-insensitive)
- real-time score tracking and percentage calculation after each question
- custom final score summary upon quiz completion
