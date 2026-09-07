# day 14 - distance coversion GUI

A simple and interactive graphical user interface (GUI) application built with Python and Tkinter that converts distances from miles to kilometers.

## how to run

```bash
uv run src/main.py
```

## skills

- **GUI Development**: Creating desktop application windows, titles, and layout structures using Python's standard `tkinter` library.
- **Tkinter Grid Manager**: Organizing UI elements using the `grid()` layout manager for precise column and row positioning, including spacer frames for alignment.
- **Dynamic State Tracking**: Utilizing `tkinter.IntVar` and `tkinter.StringVar` to bind data dynamically to label elements for automatic UI updates.
- **Event Handling & Callbacks**: Connecting user interaction (button clicks) to logic functions (conversion calculation).
- **Data Validation & Casting**: Extracting string data from user entry widgets and converting them to numbers for arithmetic processing.

## features

- **Interactive User Input**: A clean Entry field allowing users to type the number of miles they want to convert.
- **One-Click Calculation**: A "Calculate" button that processes the conversion instantly.
- **Dynamic Text Display**: Displays the conversion result dynamically within the window.
- **Grid Layout**: Well-aligned and organized layout displaying input, labels, button, and spacer components neatly.
