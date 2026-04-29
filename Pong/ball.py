from turtle import Turtle
import random

MOVEMENT = 10
RANDOM_START = [random.randint(10, 45), random.randint(315, 350), random.randint(135, 170), random.randint(190, 225)]

def deflect(angle):
    return 180 - angle * 2

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.setheading(random.choice(RANDOM_START))
        self.ball_speed = 0.1

    def move(self):
        self.forward(MOVEMENT)

    def detect_collision_border(self):
        heading = self.heading()
        if self.ycor() > 280:
            if heading > 90:
                angle = heading - 90
                self.setheading(heading + deflect(angle))
            else:
                angle = 90 - heading
                self.setheading(heading - deflect(angle) + 360)
        elif self.ycor() < -280:
            if heading > 270:
                angle = heading - 270
                self.setheading(heading + deflect(angle) - 360)
            else:
                angle = 270 - heading
                self.setheading(heading - deflect(angle))


    def detect_point_scored(self):
        return self.xcor() > 380 or self.xcor() < -380

    def reset(self):
        self.home()
        self.setheading(random.choice(RANDOM_START))
        self.ball_speed = 0.1

    def increase_speed(self):
        self.ball_speed *=.9
