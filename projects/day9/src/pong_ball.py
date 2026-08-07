import turtle as t
import random
import time

class PongBall(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

        self.default_speed = 4
        self.speed = self.default_speed
        self.backwall = False

    def serve(self):
        self.backwall = False

        self.goto(0,0)
        serve_headings = []
        serve_headings.append(random.randint(0, 45))
        serve_headings.append(random.randint(315, 360))
        serve_headings.append(random.randint(135, 180))
        serve_headings.append(random.randint(180, 225))

        serve_heading = random.choice(serve_headings)

        self.setheading(serve_heading)

        time.sleep(1.5)
        self.speed = self.default_speed


    def move(self):
        self.forward(self.speed)

    def wall_bounce(self, screen_height):
        max_y = 0.5 * screen_height
        min_y = -0.5 * screen_height

        if (min_y < self.ycor() < max_y):
            return
        else:
            angle_to_0 = self.heading()
            reverse_angle = 360 - angle_to_0

            self.setheading(reverse_angle)

    def check_backline(self, screen_width):
        limiter = 10

        max_x = 0.5 * screen_width - limiter
        min_x = -0.5 * screen_width + limiter

        if (min_x < self.xcor() < max_x):
            return
        else:
            self.speed = 0
            self.backwall = True
            print("OUT!")

    def paddle_bounce(self, screen_width, paddles):
        limiter = 40

        paddle_dists = []
        for paddle in paddles:
            distance = self.distance(paddle)
            paddle_dists.append(distance)

        min_dist = min(paddle_dists)

        max_x = 0.5 * screen_width - limiter
        min_x = -0.5 * screen_width + limiter

        if not (min_x < self.xcor() < max_x):
            if min_dist <= 50:
                angle_to_0 = self.heading()
                angle_to_90 = -(angle_to_0 - 90)
                theta = 90 + angle_to_90
                reverse_angle = theta % 360

                self.setheading(reverse_angle)
        else:
            return
