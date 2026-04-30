from turtle import Turtle

POSITION = (0, 260)
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.highscore = 0
        self.goto(POSITION)
        self.get_highscore()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)
        self.score += 1

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.put_highscore()
        self.score = 0
        self.update_score()

    def game_over(self):
        self.home()
        self.write(f"Game Over!", align=ALIGNMENT, font=FONT)

    def get_highscore(self):
        with open("data.txt", "r") as file:
            self.highscore = int(file.read())

    def put_highscore(self):
        with open("data.txt", "w") as file:
            file.write(str(self.highscore))
