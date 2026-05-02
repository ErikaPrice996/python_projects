from turtle import Turtle

class Write(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.speed(0)

    def write_state(self, state, x, y):
        self.goto(x, y)
        self.write(f"{state}", align="center", font=('Arial', 8, 'normal'))

