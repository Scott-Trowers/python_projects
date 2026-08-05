from snake_controls import init_snake, update_screen, go_up, go_down, go_left, go_right, snake_body_movement, snake_head_movement, spawn_food, is_food_eaten, off_screen, ouroboros, game_over
import turtle as t

STARTING_LENGTH = 3
SNAKE_SPEED = 25
SCREEN_HEIGHT = 700
SCREEN_WIDTH = 700

GRID_MAX_HEIGHT = int((SCREEN_HEIGHT / SNAKE_SPEED) / 2)
GRID_MIN_HEIGHT = int((SCREEN_HEIGHT / SNAKE_SPEED) / -2)

GRID_MAX_WIDTH = int((SCREEN_WIDTH / SNAKE_SPEED) / 2)
GRID_MIN_WIDTH = int((SCREEN_WIDTH / SNAKE_SPEED) / -2)

# init the required objects
snake_parts, food, screen, queued_move, delay = init_snake(snake_speed = SNAKE_SPEED,
                                                    starting_length=STARTING_LENGTH,
                                                    screen_width=SCREEN_WIDTH,
                                                    screen_height=SCREEN_HEIGHT
                                                    )

# spawn the first food
spawn_food(food,
           grid_x_coords=[GRID_MIN_WIDTH, GRID_MAX_WIDTH],
           grid_y_coords=[GRID_MIN_HEIGHT, GRID_MAX_HEIGHT],
           snake_speed=SNAKE_SPEED
           )

# begin a game
score = 0
turns = 0
game_active = True
while game_active:
    turns += 1
    snake_parts = snake_body_movement(snake_parts)
    snake_parts, queued_moves = snake_head_movement(snake_parts, queued_move, snake_speed=SNAKE_SPEED)

    food_eaten = is_food_eaten(snake_parts[0], food, snake_speed=SNAKE_SPEED)

    if food_eaten:
        score += 1

        # grow the snake
        new_snake_part = t.Turtle(shape="square")
        new_snake_part.penup()

        # start off-screen to avoid an instant collision
        new_snake_part.goto(2 * SCREEN_WIDTH, 2 * SCREEN_HEIGHT)

        snake_parts.append(new_snake_part)

        # respawn the food
        spawn_food(food,
           grid_x_coords=[GRID_MIN_WIDTH, GRID_MAX_WIDTH],
           grid_y_coords=[GRID_MIN_HEIGHT, GRID_MAX_HEIGHT],
           snake_speed=SNAKE_SPEED
           )

    update_screen(screen, delay=delay)

    # check if the snake has hit the screen boundary
    snake_off_screen = off_screen(snake_parts[0],
                                  snake_speed=SNAKE_SPEED,
                                  screen_width=SCREEN_WIDTH,
                                  screen_height=SCREEN_HEIGHT
                                  )

    # check if the snake has eaten itself after the first turn (to avoid an instant collision)
    if turns > 1:
        snake_eaten_self = ouroboros(snake_parts, snake_speed=SNAKE_SPEED)
    else:
        snake_eaten_self = False

    if snake_off_screen or snake_eaten_self:
        print(f"screen: {snake_off_screen}, eaten: {snake_eaten_self}")
        game_active = False

game_over(score, turns, snake_parts, SCREEN_WIDTH, SNAKE_SPEED)

screen.exitonclick()
