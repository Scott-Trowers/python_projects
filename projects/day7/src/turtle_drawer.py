import turtle as t

t.colormode(255)

screen = t.Screen()
screen.listen()

turt = t.Turtle()
turt.shape("turtle")
turt.speed("fastest")
turt.width(10)

keys = {"a": False, "d": False, "Left": False, "Right": False, "space": False, "c": False}

def press_a():
    keys["a"] = True

def release_a():
    keys["a"] = False


def press_d():
    keys["d"] = True

def release_d():
    keys["d"] = False


def press_left():
    keys["Left"] = True

def release_left():
    keys["Left"] = False


def press_right():
    keys["Right"] = True

def release_right():
    keys["Right"] = False


def press_space():
    keys["space"] = True

def release_space():
    keys["space"] = False


def press_c():
    keys["c"] = True

def release_c():
    keys["c"] = False


def clear_game():
    turt.home()
    turt.clear()


screen.onkeypress(press_space, "space")
screen.onkeyrelease(release_space, "space")

screen.onkeypress(press_a, "a")
screen.onkeyrelease(release_a, "a")

screen.onkeypress(press_d, "d")
screen.onkeyrelease(release_d, "d")

screen.onkeypress(press_left, "Left")
screen.onkeyrelease(release_left, "Left")

screen.onkeypress(press_right, "Right")
screen.onkeyrelease(release_right, "Right")

screen.onkeypress(clear_game, "c")

def game_state():
    if keys["space"]:
        turt.up()
    else:
        turt.down()

    if keys["c"]:
        clear_game()

    if keys["d"]:
        turt.forward(5)
    if keys["a"]:
        turt.backward(5)
    if keys["Left"]:
        turt.left(5)
    if keys["Right"]:
        turt.right(5)

    screen.update()
    screen.ontimer(game_state, 16)

game_state()
screen.mainloop()

screen.exitonclick()
