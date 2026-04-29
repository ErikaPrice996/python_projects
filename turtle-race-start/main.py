from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
starting_position = 150
ninja_turtles = []

def move_turtle(name):
    name.forward(random.randint(1, 10))


for i in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=starting_position)
    starting_position -= 50
    ninja_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in ninja_turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You Win! The {winner} turtle won the race!")
            else:
                print(f"You lost. The {winner} turtle won the race!")
            is_race_on = False
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)





screen.exitonclick()