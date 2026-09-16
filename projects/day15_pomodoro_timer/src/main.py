import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#8B0000"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLACK = '#000000'
FONT_NAME = "Ariel"
FONT_SIZE = 25
CANVAS_WIDTH=150
CANVAS_HEIGHT=150
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro Timer")
window.config(
    width=180, height=220,
    padx=30, pady=10,
    background=RED
)
window.grid_columnconfigure(1, minsize=50)

bg_img = tk.PhotoImage(file='../data/tomato_outline.png').subsample(3, 3)

canvas = tk.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=RED, highlightthickness=0)

canvas.create_image(CANVAS_WIDTH/2, CANVAS_HEIGHT/2, image=bg_img)

countdown_timer = canvas.create_text(
    CANVAS_WIDTH/2,
    CANVAS_HEIGHT/1.8,
    text="00:00",
    fill=BLACK,
    font=(FONT_NAME, FONT_SIZE, "bold")
)

canvas.grid(column=0, row=1, columnspan=3)

start_b = tk.Button(
    text="Start",
    bg=RED,
    highlightthickness=0,
    highlightbackground=RED)
start_b.grid(column=0, row=2)

ticks = tk.Label(text="✓", fg=GREEN, bg=RED, highlightthickness=0, highlightbackground=RED)
ticks.grid(column=1, row=2)

reset = tk.Button(text="Reset", bg=RED, highlightthickness=0, highlightbackground=RED)
reset.grid(column=2, row=2)

window.mainloop()