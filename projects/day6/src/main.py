import colorgram
import imageio.v2 as iio
import matplotlib.pyplot as plt
import random
import turtle as t

def extract_rgb(image_path, show_cols = False):
    img_cols = colorgram.extract(image_path, 15)
    # remove the background colours
    background_col = (img_cols[0].rgb.r, img_cols[0].rgb.g, img_cols[0].rgb.b)
    dot_cols = img_cols[2:]

    rgb_values = []
    for col in dot_cols:
        rgb_values.append([(col.rgb[0], col.rgb[1], col.rgb[2])])

    if show_cols:
        plt.imshow(rgb_values)
        plt.show()

    return rgb_values, background_col


def draw_row_of_dots(turtle, dots, cols, dot_size=50, dot_spacing=100):
    for _ in range(dots):
        random_col = random.choice(cols)[0]
        turtle.dot(dot_size, random_col)
        turtle.forward(dot_spacing)


def start_next_row(turtle, dots, dot_spacing):
    turtle.right(90)
    turtle.forward(dot_spacing)
    turtle.right(90)
    turtle.forward(dot_spacing * dots)
    turtle.right(180)


def draw_page_of_dots(turtle, rows):
    for row in range(rows):
        draw_row_of_dots(torterra, dots=7, dot_spacing=100, cols=rgb_values)
        start_next_row(torterra, dots=7, dot_spacing=100)


# display the source image
img = iio.imread("hirst_dots.png")
plt.imshow(img)
plt.show()

rgb_values, background_col = extract_rgb("hirst_dots.png")

# Turtle and Screen setup
screen = t.Screen()
t.colormode(255)

screen.bgcolor(background_col)

torterra = t.Turtle()
torterra.shape("turtle")
torterra.speed('fastest')
torterra.width(10)
torterra.hideturtle()




# begin in the top-left
torterra.penup()
torterra.goto(x=-300, y=300)

draw_page_of_dots(torterra, rows=7)

screen.exitonclick()