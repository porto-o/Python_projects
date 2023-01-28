from turtle import Turtle, Screen

porto = Turtle()
porto.shape("turtle")
porto.pd()

for i in range(0, 4):
    porto.fd(100)
    porto.left(90)
    
screen = Screen()
screen.exitonclick()
