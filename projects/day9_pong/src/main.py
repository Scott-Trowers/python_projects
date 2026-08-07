import paddles
import pong_ball
import scoreboard
import turtle as t
import time

SCORE_TARGET = 7

if __name__ == "__main__":
    screen = t.Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.listen()
    screen.title("-P-O-N-G-")
    screen.tracer(0)

    scoreboard = scoreboard.ScoreBoard()
    scoreboard.draw_score(screen.window_height())


    paddle1 = paddles.PongPaddle(player_num=1)
    paddle1.line_up(court_length=screen.window_width())

    paddle2 = paddles.PongPaddle(player_num=2)
    paddle2.line_up(court_length=screen.window_width())

    ball = pong_ball.PongBall()


    screen.onkeypress(paddle1.move_up, "w")
    screen.onkeypress(paddle1.move_down, "s")

    screen.onkeypress(paddle2.move_up, "Up")
    screen.onkeypress(paddle2.move_down, "Down")

    max_score = max([scoreboard.player1_score, scoreboard.player2_score])

    while max_score < SCORE_TARGET:
        screen.update()

        time.sleep(0.5)
        ball.serve()

        while not ball.backwall:
            ball.move()

            ball.paddle_bounce(screen.window_width(), paddles=[paddle1, paddle2])

            ball.check_backline(screen.window_width())

            ball.wall_bounce(screen.window_height())

            screen.update()
            time.sleep(0.01)

        # add scores
        if ball.xcor() < 0:
            scoreboard.player1_point(screen.window_height())
        elif ball.xcor() > 0:
            scoreboard.player2_point(screen.window_height())
        else:
            print(f"ERROR SCORING: ball pos = {ball.xcor()}")

        max_score = max([scoreboard.player1_score, scoreboard.player2_score])
        print([scoreboard.player1_score, scoreboard.player2_score])

    screen.exitonclick()
