# day 15 - pomodoro timer

A graphical Pomodoro timer application with a tomato-themed interface to help manage work sessions and break intervals.

## how to run

```bash
uv run src/main.py
```

## skills

- desktop user interface (GUI) development with `tkinter`
- canvas drawings, image scaling, and layout management using grids
- asynchronous timing and task loops with `window.after()` and `window.after_cancel()`
- dynamic application state management with tkinter variables (`tk.StringVar`)

## features

- visually clean canvas displaying a scaled tomato-outline graphic with text overlays
- standard Pomodoro phases: alternates work blocks (25 mins), short breaks (5 mins), and long breaks (20 mins)
- real-time countdown timer formatted as MM:SS
- persistent session tracking with green checkmarks indicating completed work sessions
- fully functional "Start" and "Reset" controls to run and clear the timer state
