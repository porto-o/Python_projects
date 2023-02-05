from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

game_is_on = True

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with tops
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_top()

    # Detect collision with paddle:
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 330) or (ball.distance(left_paddle) < 50 and ball.xcor() < -330):
        ball.bounce_paddle()

    # Detect when paddle misses de ball
    if ball.xcor() > 365:
        # user point
        ball.re_center()
        scoreboard.l_point()
    elif ball.xcor() < -365:
        # cpu point
        ball.re_center()
        scoreboard.r_point()



screen.exitonclick()
