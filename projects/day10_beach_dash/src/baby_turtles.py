import turtle as t

class BabyTurtle(t.Turtle):
    def __init__(self, screen_height):
        super().__init__()
        self.shape("turtle")
        self.color("oldlace")
        self.penup()
        self.setheading(90)
        self.speed = 10

        self.starting_y = (screen_height * -0.5) + 50
        self.goto(x=0, y=self.starting_y)

    def hatch(self):
        self.color("green")

    def go_forwards(self):
        self.setheading(90)
        self.forward(10)

    def go_backwards(self):
        self.setheading(90)
        self.backward(10)

    def go_left(self):
        self.setheading(180)
        self.forward(10)

    def go_right(self):
        self.setheading(0)
        self.forward(10)

    def reset_pos(self):
        self.goto(x=0, y=self.starting_y)