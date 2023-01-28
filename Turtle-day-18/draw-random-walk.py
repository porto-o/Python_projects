from turtle import Turtle, Screen
import random

# TODO
# bajar la pluma
# poner color random
# escoger un angulo random entre 90, 180 o 270
# avanzar 5 unidades
# repetir desde poner color random
# repetir todo por 20 veces

porto = Turtle()
screen = Screen()
screen.colormode(255)

porto.shape("turtle")
porto.pd()
porto.width(15)
porto.speed("fastest")
angles = [0, 90, 180, 270]


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    r_color = (red, green, blue)
    return r_color


def draw_walk(angle):
    porto.pencolor(random_color())
    porto.seth(angle)
    porto.forward(50)


for i in range(0, 201):
    draw_walk(random.choice(angles))

screen.exitonclick()
