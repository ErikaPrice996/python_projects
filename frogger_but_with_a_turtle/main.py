import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

level = 1

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()

player = Player()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")

cars = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.move(level)

    if player.complete():
        scoreboard.write_level()
        level += 1

    for car in cars.cars:
        if player.distance(car) < 25:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()