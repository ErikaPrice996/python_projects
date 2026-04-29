from turtle import Turtle
#
HEADING = 90
MOVEMENT_DIST = 20
MOVE_LIMIT = 220

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.setpos(position)
        self.shape("square")
        self.setheading(HEADING)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.penup()

    def move_up(self):
        if self.ycor() <= MOVE_LIMIT:
            self.forward(MOVEMENT_DIST)

    def move_down(self):
        if self.ycor() >= -MOVE_LIMIT:
            self.backward(MOVEMENT_DIST)
