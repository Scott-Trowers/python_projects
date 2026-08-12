import pandas as pd
import turtle as t
from states import State

states = pd.read_csv('../data/50_states.csv')

screen = t.Screen()
screen.setup(width=700, height=500)
screen.bgpic('../data/blank_states_img.gif')

prompt_msg = "Make a guess!"
guessed_states = {}
score = len(guessed_states)

while score < 50:

    guess = 'placeholder'
    while guess == 'placeholder' or guess in guessed_states.keys():
        guess = screen.textinput(title=f"Name the US States! ({score}/50)", prompt=prompt_msg)

    if guess in guessed_states.keys():
        prompt_msg = f"{guess} already named! Guess again..."
    else:
        matching_state = states[states.state.str.lower() == guess]
        if len(matching_state) > 0:
            prompt_msg = f"{guess} is correct! Guess again..."

            guessed_states[guess] = State(
                state_name=matching_state.state.values[0],
                xcor=matching_state.x.values[0],
                ycor=matching_state.y.values[0]
                )

        else:
            prompt_msg = f"{guess} is incorrect! Guess again..."

    score = len(guessed_states)

t.TK.messagebox.showinfo(title="CORRECT!", message="All 50 states names!")

screen.mainloop()
