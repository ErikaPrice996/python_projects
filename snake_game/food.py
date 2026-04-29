from turtle import Turtle
import random

FOOD_SIZE = 0.5
MAX_POSITIVE = 280
MAX_NEGATIVE = -280

class Food (Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=FOOD_SIZE, stretch_len=FOOD_SIZE)
        self.color("Yellow")
        self.speed("fastest")
        self.move()

    def move(self):
        self.goto(x=random.randint(MAX_NEGATIVE, MAX_POSITIVE), y=random.randint(MAX_NEGATIVE, MAX_POSITIVE))