import turtle as t

class ScoreBoard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.hideturtle()
        self.score = 0

    def draw_score(self, screen_height):
        self.clear()
        self.color("lightblue")
        self.goto(x=0, y=(0.5 * screen_height) - 30)
        score_message = f"Score: {self.score}"
        self.write(score_message, align="center", font=('fixedsys', 20, 'bold'))

    def next_level(self, screen_height):
        self.score += 1
        self.draw_score(screen_height)

    def game_over(self):
        game_over_msg = f"GAME OVER! Final Score: {self.score}"
        self.color("black")
        self.write(game_over_msg, align="center", font=('fixedsys', 30, 'bold'))
