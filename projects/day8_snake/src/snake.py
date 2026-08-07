import turtle as t
import time
import random

# define Snake class, inheriting Turtle()
class SnakeHead(t.Turtle):
    def __init__(self, snake_speed):
        super().__init__()
        self.speed = snake_speed

        self.snake_body = []
        self.ouroboros = False

        self.shape("square")
        self.penup()


    def hatch_snake_body(self, starting_body_length):

        for i in range(starting_body_length):
            snake_part = t.Turtle(shape="square")
            snake_part.penup()

            # separate the snake parts
            starting_y = i * self.speed
            snake_part.teleport(x=starting_y, y=0)

            self.snake_body.append(snake_part)

    def grow(self):
        new_snake_part = t.Turtle(shape="square")
        new_snake_part.penup()

        self.snake_body.append(new_snake_part)

    def head_movement(self, next_move):
        # modulo 360 to account for the circular nature of headings
        # i.e. that 270 + 180 === 270 - 180
        opposite_heading = (self.heading() + 180) % 360

        if len(next_move) == 0:
            pass
        else:
            if next_move == "forward":
                pass
            elif next_move == "up":
                if opposite_heading != 90:
                    self.setheading(90)
            elif next_move == "left":
                if opposite_heading != 180:
                    self.setheading(180)
            elif next_move == "down":
                if opposite_heading != 270:
                    self.setheading(270)
            elif next_move == "right":
                if opposite_heading != 0:
                    self.setheading(0)

        self.forward(self.speed)


    def body_movement(self):
        for snake_num in range(len(self.snake_body)):
            reverse_snake_num = -1 * snake_num

            if snake_num > 0:
                prev_part_x_coord = self.snake_body[reverse_snake_num - 1].xcor()
                prev_part_y_coord = self.snake_body[reverse_snake_num - 1].ycor()
            else:
                prev_part_x_coord = self.xcor()
                prev_part_y_coord = self.ycor()

            self.snake_body[reverse_snake_num].goto(x=prev_part_x_coord, y=prev_part_y_coord)


    def slither(self, next_move):
        self.body_movement()
        self.head_movement(next_move)


    def check_for_ouroboros(self):
        for body_part in self.snake_body:
            if self.distance(body_part) < 0.8 * self.speed:
                print(f"CLASH: {self.position()}:{body_part.position()}")

                self.ouroboros = True



class SnakePit:
    def __init__(self, screen_width, screen_height):
        self.screen = t.Screen()
        self.screen.setup(width=screen_width, height=screen_height)
        self.width = screen_width
        self.height = screen_height
        self.delay = 0.25
        self.last_input_move = []

        self.screen.bgcolor("DarkSeaGreen1")
        self.screen.title("S N A K E")
        self.screen.tracer(0)

    def select_difficulty(self):
        difficulty = 'x'
        while difficulty not in ['e', 'm', 'h']:
            difficulty = self.screen.textinput("Select Difficulty: ", "(E, M, H) ").lower()
        if difficulty == 'e':
            self.delay = 0.25
        elif difficulty == 'm':
            self.delay = 0.1
        elif difficulty == 'h':
            self.delay = 0.05


    def update_screen(self):
        self.screen.update()
        time.sleep(self.delay)


    def start_listening(self):
        self.screen.listen()

        # queue moves from key press
        self.last_input_move = ["forward"]
        self.screen.onkeypress(self.go_up, "w")
        self.screen.onkeypress(self.go_left, "a")
        self.screen.onkeypress(self.go_right, "d")
        self.screen.onkeypress(self.go_down, "s")


    def go_up(self):
        self.last_input_move  = "up"

    def go_left(self):
        self.last_input_move = "left"

    def go_right(self):
        self.last_input_move = "right"

    def go_down(self):
        self.last_input_move = "down"


    def update(self):
        self.screen.update()


    def exitonclick(self):
        self.screen.exitonclick()



class SnakeFood(t.Turtle):
    def __init__(self, screen_width, screen_height, snake_speed):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.hideturtle()

        self.max_grid_y = int((screen_height / snake_speed) / 2)
        self.min_grid_y = int((screen_height / snake_speed) / -2)

        self.max_grid_x = int((screen_width / snake_speed) / 2)
        self.min_grid_x = int((screen_width / snake_speed) / -2)

    def spawn(self, snake_speed):
        # print(f"{self.min_grid_x}, {self} ")
        rand_x = random.randint(self.min_grid_x, self.max_grid_x)
        rand_y = random.randint(self.min_grid_y, self.max_grid_y)

        self.goto(x=snake_speed * rand_x, y=snake_speed * rand_y)
        self.showturtle()



class SnakeCharmer:
    def __init__(self):
        self.score = 0
        self.turns = 0
        self.game_not_over = True

    def is_food_eaten(self, snake, food):
        if snake.distance(food) < 0.8 * snake.speed:
            print("food eaten!")
            return True
        else:
            return False

    def snake_off_screen(self, snake, screen):
        xcoord = snake.xcor()
        ycoord = snake.ycor()

        allowance = int(snake.speed * 0.75)

        x_upper_bound = (0.5 * screen.width) - allowance
        x_lower_bound = (-0.5 * screen.width) + allowance
        y_upper_bound = (0.5 * screen.height) - allowance
        y_lower_bound = (-0.5 * screen.height) + allowance

        if not (x_lower_bound < xcoord < x_upper_bound):
            self.game_not_over = False
            print(xcoord)

        if not (y_lower_bound < ycoord < y_upper_bound):
            self.game_not_over = False
            print(ycoord)

    def game_over(self, snake_speed):
        helper = t.Turtle()
        helper.hideturtle()
        helper.penup()

        screen_width = 700

        message1 = "----- GAME OVER -----"
        message2 = f"----- Score: {self.score} -----"
        message3 = f"----- Turns: {self.turns} -----"

        helper.teleport(-0.25 * screen_width, 0)
        helper.write(message1, font=('fixedsys', 20, 'bold'))

        helper.teleport(-0.25 * screen_width, -1 * snake_speed)
        helper.write(message2, font=('fixedsys', 18, 'italic'))

        helper.teleport(-0.25 * screen_width, -2 * snake_speed)
        helper.write(message3, font=('fixedsys', 18, 'italic'))


    def lets_play_snake(self, screen_width, screen_height, snake_speed, starting_length):

        pit = SnakePit(screen_width, screen_height)
        pit.select_difficulty()
        pit.start_listening()

        snake = SnakeHead(snake_speed=snake_speed)
        snake.hatch_snake_body(starting_length)

        food = SnakeFood(pit.width, pit.height, snake.speed)
        food.spawn(snake_speed=snake.speed)

        while self.game_not_over:
            self.turns += 1

            snake.slither(pit.last_input_move)

            pit.update_screen()

            if self.turns > 1:
                snake.check_for_ouroboros()
                if snake.ouroboros:
                    self.game_not_over = False

            self.snake_off_screen(snake=snake, screen=pit)

            if self.is_food_eaten(snake, food):
                self.score += 1
                food.spawn(snake_speed=snake.speed)
                snake.grow()

        self.game_over(snake.speed)

        pit.exitonclick()

if __name__ == "__main__":
    controller = SnakeCharmer()
    controller.lets_play_snake(screen_width=700, screen_height=700, snake_speed=25, starting_length=3)
