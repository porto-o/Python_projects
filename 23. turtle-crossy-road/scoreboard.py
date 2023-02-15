from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.lvl = 1
        self.color("black")
        self.pu()
        self.goto(-200, 250)
        self.hideturtle()
        self.refresh()

    def increase(self):
        self.lvl += 1
        self.clear()
        self.refresh()

    def game_over(self):
        self.goto(0, 0)
        self.write('Game over.', align="center", font=FONT)

    def refresh(self):
        self.write(f'Level: {self.lvl}', align="center", font=FONT)

