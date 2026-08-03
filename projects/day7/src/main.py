import turtle as t
import random

def UI_setup(finish_line=None):
    screen = t.Screen()
    screen.bgcolor('lightblue')

    # splinter handles the UI output
    splinter = t.Turtle()
    splinter.hideturtle()
    splinter.speed('fastest')
    splinter.penup()

    if finish_line == None:
        finish_line = screen.screensize()[0] - 100

    try:
        int(finish_line)
    except ValueError:
        print("finish_line must be an integer")

    # create a finish line marker
    finish_marker = t.Turtle()
    finish_marker.hideturtle()
    finish_marker.speed('fastest')
    finish_marker.teleport(x=finish_line, y=screen.screensize()[1] - 50)
    finish_marker.right(90)
    finish_marker.forward(2 * screen.screensize()[1])

    return screen, splinter, finish_line


def generate_turtles(turtle_names_and_colours: dict):
    turtles = {}

    for name, colour in turtle_names_and_colours.items():
        turtles[name] = t.Turtle()
        turtles[name].shape('turtle')
        turtles[name].color(colour)
        turtles[name].penup()

    return turtles

def take_prediction(turtles):
    pred = ''
    turtle_names = turtles.keys()
    nice_turtle_names = ', '.join(turtle_names).title()

    while pred not in turtle_names:
        pred = t.textinput("Which turtle will win?", f"{nice_turtle_names}?").lower()

    return pred


def turtles_to_start_line(turtles, starting_y = -200):
    starting_y = starting_y

    for name, object in turtles.items():
        object.teleport(x=-300, y=starting_y)
        starting_y += 100


def race_countdown(screen, splinter):
    for i in [3, 2, 1, 'GO!']:
        screen.delay(150)
        splinter.teleport(x=0, y=200)
        splinter.write(i, True, align="center", font=('Arial', 80, 'italic'))
        splinter.clear()


def rand_move(turtle):
    randint = random.randint(0, 10)
    turtle.forward(randint)


def run_the_race(turtles, screen, finishing_line):
    all_finished = False
    winners = {}
    turn = 0
    position = 0

    while not all_finished:
        turn += 1
        for name, object in turtles.items():
            if name not in winners.values():
                x = object.position()[0]

                if x < finishing_line:
                    rand_move(object)
                else:
                    position += 1
                    winners[position] = name

        if len(winners) == len(turtles):
            all_finished = True

        screen.delay(10)

    return winners


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


def closing_process(splinter, screen, winners, pred):
    correct_pred = (winners[1] == pred)

    screen.delay(150)
    splinter.teleport(x=0, y=200)
    splinter.write(f"{winners[1]} wins!".title(), True, align="center", font=('Arial', 60, 'italic'))

    screen.delay(150)
    splinter.teleport(x=0, y=100)
    if correct_pred:
        print("YOU WIN!")
        splinter.write("YOU WIN!", True, align="center", font=('Arial', 60, 'italic'))
    else:
        print("YOU LOSE!")
        splinter.write("YOU LOSE!", True, align="center", font=('Arial', 60, 'italic'))


def turtle_race(turtle_names_and_colours):
    screen, splinter, finish_line = UI_setup()

    turtles = generate_turtles(turtle_names_and_colours)
    pred = take_prediction(turtles)

    turtles_to_start_line(turtles)
    race_countdown(screen, splinter)
    winners = run_the_race(turtles, screen, finish_line)

    podium(winners, turtles)
    closing_process(splinter, screen, winners, pred)

    screen.exitonclick()

# name turtles and assign colour
turtle_names_and_colours = {
    "leo": "blue",
    "raphael": "red",
    "donatello": "purple",
    "michelangelo": "orange"
}

turtle_race(turtle_names_and_colours)
