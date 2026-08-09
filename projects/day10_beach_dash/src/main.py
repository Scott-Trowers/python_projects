import turtle as t
import time
import random
import baby_turtles
import crabs
import scoreboard
import background
import beach_rows

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
ROW_WIDTH = 40

screen = t.Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

scoreboard = scoreboard.ScoreBoard()

background = background.BackgroundHelper(screen_height=SCREEN_HEIGHT)
background.draw_scene(screen_height=SCREEN_HEIGHT)

turt = baby_turtles.BabyTurtle(screen_height=SCREEN_HEIGHT)

screen.onkeypress(turt.go_forwards, "w")
screen.onkeypress(turt.go_backwards, "s")
screen.onkeypress(turt.go_left, "a")
screen.onkeypress(turt.go_right, "d")

# separates c
beach_rows = beach_rows.BeachRow(screen_height=SCREEN_HEIGHT, row_width=ROW_WIDTH)

screen.bgcolor('lemonchiffon')
active_crabs = []
inactive_crabs = []

game_on = True
cycles = 0
while game_on:
    cycles += 1

    if cycles == 30:
        background.egg_hatch()
        turt.hatch()
        screen.listen()

    if cycles > 40:
        turt.color("green")

    if cycles % 3 == 0:
        spawn_count = random.randint(0, 3 + scoreboard.score)

        for i in range(spawn_count):
            active_crabs.append(crabs.Crab(
                screen_height=SCREEN_HEIGHT,
                screen_width=SCREEN_WIDTH,
                beach_rows=beach_rows
            ))

    if turt.heading() in [90, 270]:
        y_allowance = 25
    else:
        y_allowance = 20

    for index, crab in enumerate(active_crabs):
        crab.scuttle(screen_width=SCREEN_WIDTH)

        if abs(turt.ycor() - crab.ycor()) < y_allowance:
            if crab.distance(turt) < 42:
                turt.color("red")
                game_on = False

        if crab.status == "inactive":
            active_crabs.pop(index)
            inactive_crabs.append(crab)

    if turt.ycor() > 0.4 * SCREEN_HEIGHT:
        turt.color("blue")
        scoreboard.next_level(screen_height=SCREEN_HEIGHT)
        turt.reset_pos()

    time.sleep(0.1)
    screen.update()

scoreboard.game_over()
screen.mainloop()
screen.exitonclick()
