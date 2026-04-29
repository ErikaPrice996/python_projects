from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 60, "bold")
START_POSITION = (0, 0)

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.goto(position)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)
        self.score += 1

    def game_over(self):
        self.home()
        self.write(f"Game Over!", align=ALIGNMENT, font=FONT)