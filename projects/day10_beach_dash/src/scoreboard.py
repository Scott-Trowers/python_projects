import turtle as t

class ScoreBoard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.highscore = []

        self.load_highscore()

    def load_highscore(self):
        with open('../data/high_score.txt') as hscore_file:
            prev_hscore_line = hscore_file.read()

            if len(prev_hscore_line) > 0:
                prev_hscore = int(prev_hscore_line.split(' ',1)[0])
                prev_hscore_user = prev_hscore_line.split(' ',1)[1]
                print(prev_hscore)
                self.highscore = [prev_hscore, prev_hscore_user]


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
        self.goto(0,0)
        game_over_msg = (f"GAME OVER!\n"
                         f"Final Score: {self.score}\n")
        self.color("black")
        self.write(game_over_msg, align="center", font=('fixedsys', 30, 'bold'))
        if len(self.highscore) > 1:
            hs_msg = f"High Score: {self.highscore[1]} - {self.highscore[0]}"
            self.write(hs_msg, align="center", font=('fixedsys', 30, 'bold'))

    def update_high_score(self):
        if self.score > 0 and (len(self.highscore) < 2 or self.score > self.highscore[0]):
            users_name = str(t.textinput("NEW HIGH SCORE!", "Enter your name: "))
            self.highscore = [users_name, self.score]

            with open('../data/high_score.txt', mode='w') as hscore_file:
                hscore_file.write(f"{self.score} {users_name}")
