import turtle as t
import random

def random_rgb():
    rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return rgb

def draw_dashed_line(turtle, line_length, dash_length = 5, line_width=10):
    turtle.width(line_width)

    loops = int(line_length / (2 * dash_length))

    for _ in range(loops):
        turtle.forward(dash_length)
        turtle.up()
        turtle.forward(dash_length)
        turtle.down()


def draw_shape(turtle, num_sides, length = 100, col = "green", dashed_line=True, line_width=10):
    turtle.width(line_width)

    angle = 360/num_sides

    line_col = col

    for _ in range(num_sides):
        if col == "random":
            line_col = random_rgb()
        turtle.color(line_col)
        if dashed_line:
            draw_dashed_line(turtle, length)
        else:
            turtle.forward(length)
        turtle.left(angle)


def random_walk(turtle, total_length, cardinal_only=False, dashed_line=True, line_width=10):
    turtle.width(line_width)

    distance_walked = 0

    while distance_walked < total_length:
        if not cardinal_only:
            segment_length = random.randrange(1, 100)
            direction = random.randrange(0, 360)
        else:
            segment_length = 50
            direction = random.choice([0, 90, 180, 270])

        line_col = random_rgb()

        turtle.color(line_col)
        turtle.left(direction)
        if dashed_line:
            draw_dashed_line(turtle, segment_length)
        else:
            turtle.forward(segment_length)

        distance_walked += segment_length


def spirograph(turtle, num_circles, radius, line_width=10):
    turtle.width(line_width)

    direction_change = 5.5

    for _ in range(num_circles):
        turtle.left(direction_change)
        turtle.color(random_rgb())
        turtle.circle(radius)

# Turtle and Screen setup
torterra = t.Turtle()
torterra.shape("turtle")
torterra.speed('fastest')
torterra.width(10)

screen = t.Screen()
screen.bgcolor("lightblue")

t.colormode(255)

for i in range(1, 20):
    draw_shape(torterra, i, col="random", dashed_line=False)
torterra.home()

random_walk(torterra, 10000, dashed_line=False, cardinal_only=True)
torterra.home()

spirograph(torterra, 1000, 100, line_width=1)

screen.exitonclick()
