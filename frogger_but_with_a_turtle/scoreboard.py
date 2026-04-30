from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-200, 260)
        self.color("black")
        self.score = 1
        self.write_level()

    def write_level(self):
        self.clear()
        self.write(f"Level: {self.score}", align="Center", font=FONT)
        self.score += 1

    def game_over(self):
        self.home()
        self.write(f"Game Over!", align="Center", font=FONT)
