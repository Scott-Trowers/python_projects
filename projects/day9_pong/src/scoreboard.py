import turtle as t

class ScoreBoard(t.Turtle):
    def __init__(self):
        super().__init__()

        self.player1_score = 0
        self.player2_score = 0

        self.penup()
        self.hideturtle()
        self.color("white")

    def draw_score(self, screen_height):
        self.clear()
        self.goto(x=0, y=(0.5 * screen_height) - 100)
        score_message = f"{self.player1_score}     :     {self.player2_score}"
        self.write(score_message, align="center", font=('fixedsys', 40, 'bold'))

    def player1_point(self, screen_height):
        self.player1_score += 1
        self.draw_score(screen_height)

    def player2_point(self, screen_height):
        self.player2_score += 1
        self.draw_score(screen_height)
