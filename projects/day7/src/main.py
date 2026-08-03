import turtle as t
import random

screen = t.Screen()
screen.bgcolor('lightblue')

splinter = t.Turtle()
splinter.hideturtle()
splinter.speed('fastest')
splinter.penup()

FINISH_LINE = screen.screensize()[0] - 100

finish_marker = t.Turtle()
finish_marker.hideturtle()
finish_marker.speed('fastest')
finish_marker.teleport(x=FINISH_LINE, y=screen.screensize()[1]-50)
finish_marker.right(90)
finish_marker.forward(2 * screen.screensize()[1])

# generate turtles
turtles = {
    "leo": "blue",
    "raphael": "red",
    "donatello": "purple",
    "michelangelo": "orange"
}

for name, colour in turtles.items():
    turtles[name] = t.Turtle()
    turtles[name].shape('turtle')
    turtles[name].color(colour)
    turtles[name].penup()

# take prediction
pred = ''
while pred not in turtles.keys():
    pred = t.textinput("Which turtle will win?", "Leo, Raphael, Donatello, or Michelangelo").lower()

# line turtles up
starting_y = -200
for name, object in turtles.items():
    object.teleport(x=-300, y = starting_y)
    starting_y += 100

for i in [3, 2, 1, 'GO!']:
    screen.delay(150)
    splinter.teleport(x=0, y = 200)
    splinter.write(i, True, align="center", font=('Arial', 80, 'italic'))
    splinter.clear()

def rand_move(turtle):
    randint = random.randint(0, 10)
    turtle.forward(randint)


def podium(winners_dict, turtles):
    first_place = turtles[winners_dict[1]]
    second_place = turtles[winners_dict[2]]
    third_place = turtles[winners_dict[3]]

    if len(winners_dict) > 3:
        print('activated')
        for pos_num in range(4, len(winners_dict) + 1):
            print(pos_num)
            loser_turtle = turtles[winners_dict[pos_num]]
            print(loser_turtle)
            loser_turtle.teleport(1000, 1000)

    first_place.teleport(x=0, y=25)
    second_place.teleport(x=-40, y=0)
    third_place.teleport(x=35, y=-10)

all_finished = False
winners = {}
turn = 0
position = 0
while not all_finished:
    turn += 1
    for name, object in turtles.items():
        if name not in winners.values():
            x = object.position()[0]

            if x < FINISH_LINE:
                rand_move(object)
            else:
                position += 1
                winners[position] = name

    if len(winners) == len(turtles):
        all_finished = True

    screen.delay(10)

print(winners)
correct_pred = winners[1] == pred

podium(winners, turtles)

screen.delay(150)
splinter.teleport(x=0, y = 200)
splinter.write(f"{winners[1]} wins!".title(), True, align="center", font=('Arial', 60, 'italic'))
screen.delay(150)
splinter.teleport(x=0, y=100)
if correct_pred:
    print("YOU WIN!")
    splinter.write("YOU WIN!", True, align="center", font=('Arial', 60, 'italic'))
else:
    print("YOU LOSE!")
    splinter.write("YOU LOSE!", True, align="center", font=('Arial', 60, 'italic'))

screen.exitonclick()
