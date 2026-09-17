import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#8B0000"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLACK = '#000000'
FONT_NAME = "Ariel"
FONT_SIZE = 15
CANVAS_WIDTH=150
CANVAS_HEIGHT=150
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

TIMER_CYCLES = 0
active_timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global TIMER_CYCLES
    global active_timer

    window.after_cancel(active_timer)

    TIMER_CYCLES = 0
    timer_text.set("00:00")
    tick_marks.set("")

    canvas.itemconfig(countdown_text, text="Ready?")
    canvas.itemconfig(countdown_timer, text=timer_text.get())
    ticks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def timer(timer_text):
    global TIMER_CYCLES

    TIMER_CYCLES += 1

    if TIMER_CYCLES%2 != 0:
        canvas.itemconfig(countdown_text, text="Working...")
        countdown(3, timer_text)
    if TIMER_CYCLES%6 == 0:
        canvas.itemconfig(countdown_text, text="Take a break!")
        countdown(4, timer_text)
    elif TIMER_CYCLES%2 == 0:
        canvas.itemconfig(countdown_text, text="Quick break...")
        countdown(1, timer_text)

    if TIMER_CYCLES%2 == 0:
        tick_marks.set(tick_marks.get() + "✔")
        ticks.config(text=tick_marks.get())


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def parse_time(seconds, timer_text):
    m = seconds//60
    s = seconds%60
    timer_text.set(f"{m:02d}:{s:02d}")

def countdown(count, timer_text):
    global active_timer

    parse_time(count, timer_text)
    canvas.itemconfig(countdown_timer, text=timer_text.get())
    if count > 0:
        print(count)
        active_timer = window.after(1000, countdown, count - 1, timer_text)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro Timer")
window.config(
    width=180, height=220,
    padx=30, pady=10,
    background=RED
)
window.grid_columnconfigure(1, minsize=50)

# background image
bg_img = tk.PhotoImage(file='../data/tomato_outline.png').subsample(3, 3)
canvas = tk.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=RED, highlightthickness=0)
canvas.create_image(CANVAS_WIDTH/2, CANVAS_HEIGHT/2, image=bg_img)

# timer
timer_text = tk.StringVar(value="00:00")
state_text = tk.StringVar(value="Ready?")

countdown_text = canvas.create_text(
    CANVAS_WIDTH/2,
    CANVAS_HEIGHT/1.95,
    text=state_text.get(),
    fill=BLACK,
    font=(FONT_NAME, FONT_SIZE, "italic")
)
countdown_timer = canvas.create_text(
    CANVAS_WIDTH/2,
    CANVAS_HEIGHT/1.5,
    text=timer_text.get(),
    fill=BLACK,
    font=(FONT_NAME, FONT_SIZE, "bold")
)
canvas.grid(column=0, row=1, columnspan=3)

# start and reset buttons
start_b = tk.Button(
    text="Start",
    bg=RED,
    highlightthickness=0,
    highlightbackground=RED,
    command=lambda: timer(timer_text=timer_text)
)
start_b.grid(column=0, row=2)

# ticks
tick_marks = tk.StringVar(value="")

ticks = tk.Label(text=tick_marks.get(), fg=GREEN, bg=RED, highlightthickness=0, highlightbackground=RED)
ticks.grid(column=1, row=2)

reset = tk.Button(text="Reset", bg=RED, highlightthickness=0, highlightbackground=RED,
                  command=reset_timer
                  )
reset.grid(column=2, row=2)

window.mainloop()
