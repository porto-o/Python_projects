from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.create_paddle(x_cor, y_cor)

    def create_paddle(self, x_cor, y_cor):
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.shape("square")
        self.seth(90)
        self.goto(x_cor, y_cor)
        self.shapesize(stretch_len=5, stretch_wid=1)

    def up(self):
        self.seth(90)
        self.fd(20)

    def down(self):
        self.seth(270)
        self.fd(20)
