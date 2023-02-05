from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.pu()
        self.goto(0, 265)
        self.hideturtle()
        self.refresh()

    def refresh(self):
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def increase(self):
        self.score += 1
        self.clear()
        self.refresh()

    def game_over(self):
        self.goto(0, 0)
        self.write('Game over.', align=ALIGNMENT, font=FONT)
