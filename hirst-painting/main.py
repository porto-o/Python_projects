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
porto.goto(0,0)
screen = Screen()
screen.screensize(50,50)
screen.colormode(255)

for dot in range(0, 11):
    porto.dot(40, random.choice(list_colors))
    porto.fd(100)

screen.exitonclick()
