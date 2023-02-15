import random
from turtle import Turtle, Screen

# 100 en longitud
# triangle 360 / 3

porto = Turtle()
porto.pd()

colors = ["red", "rebecca purple", "dark orange", "spring green", "light sky blue"]

def draw_shapes(number_of_sides):
    angle = 360 / number_of_sides
    for i in range(0, number_of_sides):
        porto.pencolor(random.choice(colors))
        porto.right(angle)
        porto.forward(100)


for number in range(3, 11):
    draw_shapes(number)

screen = Screen()
screen.exitonclick()
