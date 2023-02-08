from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.read_file()
        self.color("white")
        self.pu()
        self.goto(0, 265)
        self.hideturtle()
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f'Score: {self.score} Highscore: {self.highscore}', align=ALIGNMENT, font=FONT)

    def increase(self):
        self.score += 1
        self.refresh()

    def reset(self):
        if self.score > int(self.highscore):
            self.highscore = self.score
            self.save_high_score()
        self.score = 0
        self.refresh()

    def save_high_score(self):
        with open("Snake_game\high_score.txt", mode="w") as file:
            file.write(f'{self.score}')

    def read_file(self):
        with open("Snake_game\high_score.txt") as file:
            high = int(file.read())
        return high