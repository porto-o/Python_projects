import random
import colorgram
from turtle import Turtle, Screen

colors = colorgram.extract("./example.jpg", 10)
list_colors = []
for color in colors:
    current_color = color.rgb
    color_tuple = (current_color[0], current_color[1], current_color[2])
    list_colors.append(color_tuple)

porto = Turtle()
porto.penup()
porto.hideturtle()
porto.speed('fast')
screen = Screen()
screen.colormode(255)
number_dots = 100

porto.seth(225)
porto.fd(300)
porto.seth(0)

for dot in range(1, number_dots + 1):
    porto.dot(20, random.choice(list_colors))
    porto.fd(50)

    if dot % 10 == 0:
        porto.seth(90)
        porto.fd(50)
        porto.seth(180)
        porto.fd(500)
        porto.seth(0)


screen.exitonclick()
