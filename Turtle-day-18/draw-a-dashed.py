from turtle import Turtle, Screen

porto = Turtle()

for i in range(0, 10):
    porto.pd()
    porto.forward(5)
    porto.up()
    porto.forward(5)

screen = Screen()
screen.exitonclick()
