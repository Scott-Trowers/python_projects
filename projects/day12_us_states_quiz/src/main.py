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

game_active = True

while game_active:

    guess = 'placeholder'
    while guess == 'placeholder':
        guess = screen.textinput(title=f"Name the US States! ({score}/50)", prompt=prompt_msg).title()

    if guess in guessed_states.keys():
        prompt_msg = f"{guess} already named! Guess again..."
    elif guess == 'Exit':
        game_active = False
    else:
        matching_state = states[states.state.str.title() == guess]
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

    if score == 50:
        game_active = False

if score == 50:
    t.TK.messagebox.showinfo(title="You Win!", message="All 50 states named!")
else:
    t.TK.messagebox.showinfo(title="Not Quite!", message=f"You named {score} out of 50 states!")

answer_key = states[['state']].copy()
answer_key['guessed'] = (answer_key.state.isin(guessed_states.keys()))
answer_key = answer_key.sort_values(['guessed', 'state'], ascending=[False, True])

print(f"You named {score} out of 50 states!\n")
print(answer_key)

answer_key.to_csv('../data/last_game_results.csv', index=False)

screen.mainloop()
