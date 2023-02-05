from turtle import Turtle, Screen

porto = Turtle()


def draw_fd():
    porto.fd(10)


def draw_bd():
    porto.backward(10)


def turn_right():
    porto.right(10)


def turn_left():
    porto.left(10)


def clear():
    porto.reset()


screen = Screen()
screen.listen()
screen.onkey(fun=draw_fd, key='w')
screen.onkey(fun=draw_bd, key='s')
screen.onkey(fun=turn_right, key='d')
screen.onkey(fun=turn_left, key='a')
screen.onkey(fun=clear, key='c')

screen.exitonclick()
