import tkinter as tk
from tkinter import messagebox
import pandas as pd
import random

BACKGROUND_COLOR = 'goldenrod1'
ACCENT_COLOUR = 'red2'
TOP_N_WORDS = 100

spanish_words_path = '../data/spanish_common_words.csv'
known_words_path = '../data/known_words.txt'


def load_words():
    spanish_words_df = pd.read_csv(spanish_words_path)

    try:
        with open(known_words_path, mode='r') as f:
            known_words = f.read().splitlines()
    except FileNotFoundError:
        known_words = []

    spanish_words_df = spanish_words_df.loc[~spanish_words_df.spanish_word.isin(known_words)]
    spanish_words_df.reset_index(inplace=True, drop=True)

    return spanish_words_df[0:TOP_N_WORDS]


def save_known_word(known_word):
    with open(known_words_path, mode='a') as f:
        f.write(known_word)
        f.write('\n')


def check_progress():
    global selected_words

    if len(selected_words) == 0:
        messagebox.showinfo(title="Password Search", message="All words complete!\nLoading new words...")
        selected_words = load_words()
        count_rem_words()


def random_word():
    global selected_words

    current_index.set(random.randint(0, len(selected_words)-1))
    print(f"rand ind: {current_index.get()}")

    current_spanish_word.set(selected_words.iloc[current_index.get(), 0])
    current_english_translation.set(selected_words.iloc[current_index.get(), 1])


def new_word():
    random_word()
    card_canvas.itemconfig(word_text, text=current_spanish_word.get())

def count_rem_words():
    global selected_words

    card_count.set(len(selected_words))

    card_count_msg.set(f"Remaining Cards: {card_count.get()}/{TOP_N_WORDS}")
    card_canvas.itemconfig(card_count_text, text=card_count_msg.get())


def remove_word():
    global selected_words

    save_known_word(current_spanish_word.get())

    selected_words.drop([current_index.get()], inplace=True)
    selected_words.reset_index(inplace=True, drop=True)

    count_rem_words()


def cross_func():
    print("Return card")
    new_word()


def tick_func():
    print("Remove card")
    remove_word()
    check_progress()
    new_word()


selected_words = load_words()

window = tk.Tk()
window.title("Spanish Flashcards")
window.config(
    bg=BACKGROUND_COLOR,
    width=500,
    height=400,
    padx=50,
    pady=30
)

current_index = tk.IntVar()
current_spanish_word = tk.StringVar()
current_english_translation = tk.StringVar()

card_count = tk.IntVar(value=TOP_N_WORDS)

card_count_msg = tk.StringVar(value=f"Remaining Cards: {card_count.get()}/{TOP_N_WORDS}")

card_canvas = tk.Canvas(
    width=400,
    height=200,
    bg=BACKGROUND_COLOR,
    highlightbackground=ACCENT_COLOUR,
)

word_text = card_canvas.create_text(
    200,
    100,
    text=f'"{current_spanish_word.get()}"',
    fill=ACCENT_COLOUR,
    font=('Arial', 22, "bold")
)

card_count_text = card_canvas.create_text(
    200,
    20,
    text=card_count_msg.get(),
    fill=ACCENT_COLOUR,
    font=('Arial', 12, "italic")
)

card_canvas.grid(column=0, row=0, columnspan=3)

new_word()

cross_button = tk.Label(
    text="❎",
    bg=BACKGROUND_COLOR,
    fg=BACKGROUND_COLOR,
    font=('Arial', 22, "italic")
)
cross_button.bind("<Button-1>", lambda e: cross_func())
cross_button.grid(column=0, row=1, pady=(20, 0))

tick_button = tk.Label(
    text="✅",
    bg=BACKGROUND_COLOR,
    fg=BACKGROUND_COLOR,
    font=('Arial', 22, "italic")
)
tick_button.bind("<Button-1>", lambda e: tick_func())
tick_button.grid(column=2, row=1, pady=(20, 0))





window.mainloop()
