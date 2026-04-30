from turtle import Turtle
import random

from requests import delete

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
#
# STARTING_POSITION = (random.randint(a=-400, b=400), random.randint(a=-250, b=250))


class CarManager:
    def __init__(self):
        self.cars = []
        for _ in range(50):
            self.init_car()

    def new_car(self):
        car = Turtle()
        car.hideturtle()
        car.shape("square")
        car.color(random.choice(COLORS))
        car.penup()
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.speed(0)
        return car

    def setup (self, car):
        car.speed(1)
        car.showturtle()
        return car

    def init_car(self):
        car = self.new_car()
        car.goto(random.randrange(-300, 1400, 20), random.randrange(-250, 250, 20))
        car = self.setup(car)
        self.cars.append(car)

    def move(self, level):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * (level - 1)))
            if car.xcor() < -360:
                ycor = car.ycor()
                self.cars.remove(car)
                new_car = self.new_car()
                new_car.goto(1400, ycor)
                new_car = self.setup(new_car)
                self.cars.append(new_car)


