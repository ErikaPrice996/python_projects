from turtle import Turtle, Screen

from colorama.ansi import clear_screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def circle_counter_clockwise():
    tim.circle(100, 10, 10)

def circle_clockwise():
    tim.circle(-100, 10, 10)

def rotate_left():
    tim.left(5)

def rotate_right():
    tim.right(5)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.setpos(0, 0)
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="q", fun=circle_counter_clockwise)
screen.onkey(key="e", fun=circle_clockwise)
screen.onkey(key="c", fun=clear_screen)
screen.onkey(key="a", fun=rotate_left)
screen.onkey(key="d", fun=rotate_right)

screen.exitonclick()
