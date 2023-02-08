from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []  # the snake or segment is the collection of turtle objects
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        turtle = Turtle(shape="square")
        turtle.color("white")
        turtle.pu()
        turtle.goto(position)
        self.segments.append(turtle)

    def extend(self):
        # add a new segment to the snake
        self.add_segment(self.segments[-1].position())

    def move(self):
        # How do we turn our snake?
        # we move the predecessor segment to the position of its successor
        # Thus, we just need to update the orientation of the first, while the others are just taking other positions
        # starting from the last turtle in the snake (the last that was appended)
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # Coordinates of the turtle from second to last
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        # moving the first turtle
        self.head.fd(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(0)
        
    def reset(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
    

