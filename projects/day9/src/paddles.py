import turtle as t

class PongPaddle(t.Turtle):
    def __init__(self, player_num, length=4):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.speed = 20
        self.player_num = player_num

        self.length = length
        self.shapesize(stretch_wid=1, stretch_len=self.length, outline=None)

    def line_up(self, court_length):
        if self.player_num not in [1, 2]:
            print("ERROR! INVALID PLAYER_NUM")

        # leave a small gap between the paddle and court edge
        adjusted_court_length = int(round(court_length * 0.95, 0))

        # -1 reduces the player_num to 0 or 1, and -0.5 splits the court length in two
        side = (self.player_num - 1 - 0.5) * adjusted_court_length
        self.goto(x=side, y=0)

    def move_up(self):
        self.forward(self.speed)

    def move_down(self):
        self.backward(self.speed)
