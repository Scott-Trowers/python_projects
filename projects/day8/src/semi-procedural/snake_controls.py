import turtle as t
import time
import random


# create the snake, screen, and take user difficu
def init_snake(starting_length, snake_speed, screen_width, screen_height):
    """
    initialises the starting snake, the screen, and sets the difficulty speed

    :param starting_length: how long the snake should begin as
    :param snake_speed: how far the snake will move each turn
    :param screen_width: how wide the screen should be
    :param screen_height: how tall the screen should be
    :return: the snake parts (dict), the food, the screen, the first move, and the difficulty speed
    """

    # screen = t.Screen()
    # screen.setup(width=screen_width, height=screen_height)
    # screen.bgcolor("DarkSeaGreen1")
    # screen.title("S N A K E")
    #
    # difficulty = 'x'
    # while difficulty not in ['e', 'm', 'h']:
    #     difficulty = screen.textinput("Select Difficulty: ", "(E, M, H) ").lower()
    # if difficulty == 'e':
    #     delay = 0.25
    # elif difficulty == 'm':
    #     delay = 0.1
    # elif difficulty == 'h':
    #     delay = 0.05

    # turn tracer off for smoother animation (i.e. so we can move all segments, then update the screen)
    # screen.tracer(0)

    # screen.listen()

    # queue moves from key press
    queued_move = ["forward"]
    # screen.onkeypress(lambda: go_up(queued_move), "w")
    # screen.onkeypress(lambda: go_left(queued_move), "a")
    # screen.onkeypress(lambda: go_right(queued_move), "d")
    # screen.onkeypress(lambda: go_down(queued_move), "s")

    # snake_parts = []
    # for i in range(starting_length):
    #
    #     snake_part = t.Turtle(shape="square")
    #     snake_part.penup()
    #
    #     # separate the snake parts
    #     starting_y = i * snake_speed
    #     snake_part.teleport(x=starting_y, y=0)
    #
    #     snake_parts.append(snake_part)

    # food = t.Turtle(shape="circle", visible=False)
    # food.penup()

    return snake_parts, food, screen, queued_move, delay


def update_screen(screen, delay):
    """
    Updates the screen, with a delay to prevent blurring
    """
    # screen.update()
    # time.sleep(delay)


# queues the next move according to a key press



def snake_head_movement(snake_parts, queued_move, snake_speed):
    """
    Sets the snake's head's direction according to the last key press,
    while preventing the snake turning back directly on itself
    """
    # snake_head = snake_parts[0]
    # current_heading = snake_head.heading()
    #
    # # modulo 360 to account for the circular nature of headings
    # # i.e. that 270 + 180 === 270 - 180
    # opposite_heading = (current_heading + 180) % 360


    # if (len(queued_move) == 0):
    #     pass
    # else:
    #     next_move = queued_move[0]
    #
    #     if (next_move == "forward"):
    #         pass
    #     elif next_move == "up":
    #         if opposite_heading != 90:
    #             snake_head.setheading(90)
    #     elif next_move == "left":
    #         if opposite_heading != 180:
    #             snake_head.setheading(180)
    #     elif next_move == "down":
    #         if opposite_heading != 270:
    #             snake_head.setheading(270)
    #     elif next_move == "right":
    #         if opposite_heading != 0:
    #             snake_head.setheading(0)
    #     else:
    #         print("!!ERROR!! INVALID MOVE")
    #
    # snake_head.forward(snake_speed)

    return snake_parts, queued_move


def snake_body_movement(snake_parts):
    """ Moves the snake_body parts to follow the previous location of the next part up the snake."""
    # for snake_num in range(1, len(snake_parts)):
    #     reverse_snake_num = -1 * snake_num
    #     prev_part_x_coord = snake_parts[reverse_snake_num - 1].xcor()
    #     prev_part_y_coord = snake_parts[reverse_snake_num - 1].ycor()
    #     snake_parts[reverse_snake_num].goto(x=prev_part_x_coord, y=prev_part_y_coord)

    return snake_parts


def spawn_food(food_object, grid_x_coords, grid_y_coords, snake_speed):
    """ Randomly spawns food within the screen """
    # max_x = grid_x_coords[1] - 1
    # min_x = grid_x_coords[0] + 1
    #
    # max_y = grid_y_coords[1] - 1
    # min_y = grid_y_coords[0] + 1
    #
    # rand_x = random.randint(min_x, max_x)
    # rand_y = random.randint(min_y, max_y)
    #
    # food_object.goto(x=snake_speed * rand_x, y=snake_speed * rand_y)
    # food_object.showturtle()


def is_food_eaten(snake_head, food_object, snake_speed):
    """ Checks if the snake's head is over the food."""
    # if snake_head.distance(food_object) < 0.8 * snake_speed:
    #     print("food eaten!")
    #     return True
    # else:
    #     return False


def off_screen(snake_head, snake_speed, screen_width, screen_height):
    """ Checks if the snake's head is off the screen"""
    # xcoord = snake_head.xcor()
    # ycoord = snake_head.ycor()
    #
    # allowance = int(snake_speed * 0.75)
    #
    # x_upper_bound = (0.5 * screen_width) - allowance
    # x_lower_bound = (-0.5 * screen_width) + allowance
    # y_upper_bound = (0.5 * screen_height) - allowance
    # y_lower_bound = (-0.5 * screen_height) + allowance

    # if not (x_lower_bound < xcoord < x_upper_bound):
    #     outside_boundaries = True
    #     print(xcoord)
    #     return outside_boundaries
    #
    # if not (y_lower_bound < ycoord < y_upper_bound):
    #     outside_boundaries = True
    #     print(ycoord)
    #     return outside_boundaries
    #
    # outside_boundaries = False
    # return outside_boundaries


def ouroboros(snake_parts, snake_speed):
    """ Checks if the snake's head is touching another part of the snake."""
    snake_head = snake_parts[0]

    for part_num in range(1, len(snake_parts)):
        segment = snake_parts[part_num]

        # if snake_head.distance(segment) < 0.8 * snake_speed:
        #     print(f"{part_num} clash!")
        #     print(f"{snake_head.position()}:{segment.position()}")
        #
        #     ouroboros = True
        #     return ouroboros

    ouroboros = False
    return ouroboros


def game_over(score, turns, snake_parts, screen_width, snake_speed):
    "Prints a game over message and stats."
    # message1 = "----- GAME OVER -----"
    # message2 = f"----- Score: {score} ---"
    # message3 = f"----- Turns: {turns} ---"
    #
    # snake_parts[0].teleport(-0.25 * screen_width, 0)
    # snake_parts[0].write(message1, font=('fixedsys', 20, 'bold'))
    #
    # snake_parts[0].teleport(-0.25 * screen_width, -1 * snake_speed)
    # snake_parts[0].write(message2, font=('fixedsys', 20, 'bold'))
    #
    # snake_parts[0].teleport(-0.25 * screen_width, -2 * snake_speed)
    # snake_parts[0].write(message3, font=('fixedsys', 20, 'bold'))

    return message1, message2, message3
