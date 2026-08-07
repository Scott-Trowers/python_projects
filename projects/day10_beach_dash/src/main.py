import turtle as t
import time
import random
import baby_turtles
import crabs
import beach_rows
from projects.day10_beach_dash.src.beach_rows import BeachRow

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
ROW_WIDTH = 40

screen = t.Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

turt = baby_turtles.BabyTurtle(screen_height=SCREEN_HEIGHT)

screen.listen()

screen.onkeypress(turt.go_forwards, "w")
screen.onkeypress(turt.go_backwards, "s")
screen.onkeypress(turt.go_left, "a")
screen.onkeypress(turt.go_right, "d")

beach_rows = BeachRow(screen_height=SCREEN_HEIGHT, row_width=ROW_WIDTH)

screen.bgcolor('lemonchiffon')
active_crabs = []

game_on = True

while game_on:
    spawn_count = random.randint(0, 3)

    for i in range(spawn_count):
        active_crabs.append(crabs.Crab(
            screen_height=SCREEN_HEIGHT,
            screen_width=SCREEN_WIDTH,
            beach_rows=beach_rows
        ))

    for crab in active_crabs:
        crab.scuttle(screen_width=SCREEN_WIDTH)

    print(active_crabs[0].pos())

    time.sleep(0.1)
    screen.update()

screen.mainloop()
screen.exitonclick()
