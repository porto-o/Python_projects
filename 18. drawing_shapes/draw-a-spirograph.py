from turtle import Turtle, Screen

"""
    Process of drawing the spirograph:
    
    - We pass the size of the gap to the function that draws the spirograph
        note: the size of the gap is the space that exist between the circles,
        the more space, the less circles are
    - To complete the circle we have to turn 360 degrees, so we declare the for
    - The for steps will be the size of the gap, thus the angle of turn will be the same
    - just print the circle
    
    We can have more circles just by passing a minor number to the function
"""

porto = Turtle()
screen = Screen()
porto.speed("fastest")


def draw_spirograph(size_of_gap):
    for i in range(0, 361, size_of_gap):
        porto.circle(100)
        porto.seth(i)
    print("I finish jeje")


draw_spirograph(1)
screen.exitonclick()
