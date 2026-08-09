import turtle as t

class BackgroundHelper(t.Turtle):
    def __init__(self, screen_height):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0

        self.starting_y = (screen_height * -0.5) + 50


    def draw_scene(self, screen_height):
        self.color("blue")
        self.shape("square")
        self.turtlesize(stretch_wid=5, stretch_len=2000, outline=True)
        self.goto(x=0, y=0.47 * screen_height)
        self.stamp()

        self.goto(x=0, y=self.starting_y)

        self.shape("circle")
        self.color("black")
        self.turtlesize(stretch_wid=2.52, stretch_len=1.52, outline=True)
        self.stamp()

        self.color("oldlace")
        self.turtlesize(stretch_wid=2.5, stretch_len=1.5, outline=True)
        self.stamp()

    def egg_hatch(self):
        self.goto(x=40, y=self.starting_y)
        self.color("black")
        self.write("CrrracK!", align="center", font=('fixedsys', 10, 'italic'))
