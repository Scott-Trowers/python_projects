import turtle as t
import random

class Crab(t.Turtle):
    def __init__(self, screen_height, screen_width, beach_rows):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3, outline=None)
        self.color(self.random_rgb())
        self.penup()

        # randomise speed
        self.speed = random.randint(5, 10)

        # randomise starting point
        self.starting_row_num = random.randint(0, len(beach_rows.rows)-1)
        self.starting_side = beach_rows.rows[self.starting_row_num]

        # leave a buffer at either side of the screen
        if (5 < self.starting_row_num < len(beach_rows.rows) - 6):

            if self.starting_side == -1:
                self.setheading(0)
            else:
                self.setheading(180)

            starting_x = self.starting_side * (int(0.5 * screen_width)  + 100)
            starting_y = (self.starting_row_num * beach_rows.row_width) - 0.5 * screen_height
        else:
            self.speed = 0
            starting_x = 99999
            starting_y = 99999

        self.goto(x=starting_x, y=starting_y)

    def random_rgb(self):
        t.colormode(255)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        return (r, g, b)

    def scuttle(self, screen_width):
        if self.starting_side == -1:
            max_x = 0.5 * screen_width
            if self.xcor() < max_x:
                self.forward(self.speed)
        else:
            max_x = -0.5 * screen_width
            if self.xcor() > max_x:
                self.forward(self.speed)
