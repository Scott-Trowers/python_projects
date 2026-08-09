import turtle as t
import random

class Crab(t.Turtle):
    def __init__(self, screen_height, screen_width, beach_rows):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3, outline=None)
        self.color(self.random_crab_col())
        self.penup()
        self.status = "active"

        # randomise speed
        self.speed = random.randint(5, 10)

        # randomise starting point
        self.starting_row_num = random.randint(0, len(beach_rows.rows)-1)
        self.starting_side = beach_rows.rows[self.starting_row_num]

        # leave a buffer at either side of the screen
        starting_y = (self.starting_row_num * beach_rows.row_width) - 0.5 * screen_height
        starting_x = self.starting_side * (int(0.5 * screen_width) + 100)

        if (-0.4 * screen_height < starting_y < 0.4 * screen_height):
            if self.starting_side == -1:
                self.setheading(0)
            else:
                self.setheading(180)
        else:
            self.speed = 0
            starting_x = 99999
            starting_y = 99999

        self.goto(x=starting_x, y=starting_y)

    def random_crab_col(self):
        cols = ["orange", "pink", "crimson", "coral", "deeppink"]
        chosen_col = random.choice(cols)
        return chosen_col

    def scuttle(self, screen_width):
        if self.starting_side == -1:
            max_x = 0.6 * screen_width

            # stop if out of bounds
            if self.xcor() < max_x:
                self.forward(self.speed)
            else:
                self.status = "inactive"
        else:
            max_x = -0.6 * screen_width
            if self.xcor() > max_x:
                self.forward(self.speed)
            else:
                self.status = "inactive"
