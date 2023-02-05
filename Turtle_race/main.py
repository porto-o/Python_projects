from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_prompt = screen.textinput(title="Your bet", prompt="Which turtle will win the race? enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False
list_turtles = []


y_pos = -80
for color in colors:
    turtle = Turtle(shape='turtle')
    turtle.pu()
    turtle.color(color)
    turtle.goto(x=-230, y=y_pos)
    y_pos += 30
    list_turtles.append(turtle)

if user_prompt:
    is_race_on = True

while is_race_on:
    for turtle in list_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_color = turtle.pencolor()
            if user_prompt == winner_color:
                print(f'You have won! the {winner_color} turtle is the winner! ')
            else:
                print(f'You have lost!, the {winner_color} turtle is the winner!')

        random_distance = random.randint(0, 10)  # distance of turtle is moving fd
        turtle.fd(random_distance)

screen.exitonclick()
