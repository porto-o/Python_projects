from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.pu()
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.color("orange")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
