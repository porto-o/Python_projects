from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

"""
    TODO
    1. Create snake body - :)
    2. Move the snake - :)
    3. Control de snake using keyboard controls - :)
    4. Detect collision with food - :)
    5. Create a scoreboard - :)
    6. Detect collision with wall - :)
    7. Detect collision with tail - :)
"""
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
# To turn off the animation of moving forwards we use tracer() method
# tracer turn turtle animation on or off
# we must use update method to see the turtles after their moves


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    # Detect collision with food by using distance method from Turtle module
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
    # if head collides with any segment in the tail
    # game over

screen.exitonclick()
