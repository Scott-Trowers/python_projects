import turtle as t

class State(t.Turtle):
    def __init__(self, state_name, xcor, ycor):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("green")
        self.teleport(x=xcor, y=ycor)
        self.write(state_name, move=False, align='center', font=('Arial', 8, 'normal'))
