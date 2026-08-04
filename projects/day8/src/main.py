import turtle as t
import time
import random

"""
1) Create snake body
2) move the snake
    if queued_moves is empty, move forward
    else move according to the objects queued move
3) create food
4) 'consume' the food and grow
5) detect collision with a wall or tail
6) create a scoreboard
"""

STARTING_LENGTH = 3
SNAKE_SPEED = 25
SCREEN_HEIGHT = 700
SCREEN_WIDTH = 700

GRID_MAX_HEIGHT = int((SCREEN_HEIGHT / SNAKE_SPEED) / 2)
GRID_MIN_HEIGHT = int((SCREEN_HEIGHT / SNAKE_SPEED) / -2)

GRID_MAX_WIDTH = int((SCREEN_WIDTH / SNAKE_SPEED) / 2)
GRID_MIN_WIDTH = int((SCREEN_WIDTH / SNAKE_SPEED) / -2)


screen = t.Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("DarkSeaGreen1")
screen.title("S N A K E")

# turn tracer off for smoother animation (i.e. so we can move all segments, then update the screen)
screen.tracer(0)

screen.listen()

# create the snake body
snake_parts = []
for i in range(STARTING_LENGTH):

    snake_part = t.Turtle(shape="square")
    snake_part.penup()

    # separate the snake parts
    starting_y = i * SNAKE_SPEED
    snake_part.teleport(x=starting_y, y=0)

    snake_parts.append(snake_part)

queued_moves = []

def update_screen(screen, delay = 0.25):
    screen.update()
    time.sleep(delay)


# queue moves from key press
def go_up():
    queued_moves.append("up")
    return "up"


def go_left():
    queued_moves.append("left")
    return "left"


def go_right():
    queued_moves.append("right")
    return "right"


def go_down():
    queued_moves.append("down")
    return "down"

screen.onkeypress(go_up, "w")
screen.onkeypress(go_left, "a")
screen.onkeypress(go_right, "d")
screen.onkeypress(go_down, "s")


def snake_head_movement(snake_parts, queued_moves):
    snake_head = snake_parts[0]

    if (len(queued_moves) == 0):
        pass
    else:
        if (queued_moves[0] == "forward"):
            pass
        elif queued_moves[0] == "up":
            snake_head.setheading(90)
        elif queued_moves[0] == "left":
            snake_head.setheading(180)
        elif queued_moves[0] == "down":
            snake_head.setheading(270)
        elif queued_moves[0] == "right":
            snake_head.setheading(0)
        else:
            print("!!ERROR!! INVALID MOVE")

        queued_moves.pop(0)

    snake_head.forward(SNAKE_SPEED)

    return snake_parts, queued_moves


def snake_body_movement(snake_parts):
    for snake_num in range(1, len(snake_parts)):
        reverse_snake_num = -1 * snake_num
        prev_part_x_coord = snake_parts[reverse_snake_num - 1].xcor()
        prev_part_y_coord = snake_parts[reverse_snake_num - 1].ycor()
        snake_parts[reverse_snake_num].goto(x=prev_part_x_coord, y=prev_part_y_coord)

    return snake_parts


food = t.Turtle(shape="circle", visible=False)
food.penup()
def spawn_food(food_object):
    max_x = GRID_MAX_WIDTH - 1
    min_x = GRID_MIN_WIDTH + 1

    max_y = GRID_MAX_HEIGHT - 1
    min_y = GRID_MIN_HEIGHT + 1

    rand_x = random.randint(min_x, max_x)
    rand_y = random.randint(min_y, max_y)

    food_object.goto(x=SNAKE_SPEED * rand_x, y=SNAKE_SPEED * rand_y)
    food_object.showturtle()


def is_food_eaten(snake_head, food_object, food_eaten):
    print("Snake at: ", snake_head.position())
    print("Food at: ", food_object.position())
    snake_x_cord = int(snake_head.xcor())
    snake_y_cord = int(snake_head.ycor())
    food_x_cord = int(food_object.xcor())
    food_y_cord = int(food_object.ycor())

    same_x = (snake_x_cord == food_x_cord)
    same_y = (snake_y_cord == food_y_cord)
    if same_x and same_y:
        print("food eaten!")
        return True

game_active = True
spawn_food(food)
score = 0
while game_active:
    food_eaten = False
    snake_parts = snake_body_movement(snake_parts)
    snake_parts, queued_moves = snake_head_movement(snake_parts, queued_moves)

    food_eaten = is_food_eaten(snake_parts[0], food, food_eaten)
    if food_eaten == True:
        score += 1

        new_snake_part = t.Turtle(shape="square")
        new_snake_part.penup()
        new_snake_part.goto(snake_parts[0].position())

        snake_parts.append(new_snake_part)

        spawn_food(food)

    update_screen(screen)




# TODO remove queue - just take last insructions
# TODO if move would be the opposite ßheading to the previous direction, ignore it
# TODO lose when snake touches border
# TODO lose when snake touches itself
# TODO game over screen
# TODO tidy into classes


screen.exitonclick()
