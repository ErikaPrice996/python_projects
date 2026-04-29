import colorgram as cg
import random
import turtle

def random_color():
    return random.choice(color_palette)

def set_start_position(x, y):
    t.penup()
    t.setx(x)
    t.sety(y)
    t.pendown()

def paint_lines(num_lines, num_dots):
    for i in range(num_lines):
        for j in range(num_dots):
            t.dot(20, random_color())
            t.forward(60)
        t.left(90)
        t.forward(60)
        t.left(90)
        t.forward(60 * num_dots)
        t.left(180)

# colors = cg.extract('image.jpg', 10)
# color_palette = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_palette.append((r, g, b))
#
# print(color_palette)
color_palette = [(225, 233, 238), (143, 26, 67), (237, 72, 37), (220, 164, 55), (15, 140, 88), (174, 162, 50)]

#init
t = turtle.Turtle()
screen = turtle.Screen()

#define variables
t.shape("turtle")
t.color("DarkSlateGray1")
t.speed("fastest")
screen.colormode(255)
screen.bgcolor("aquamarine")
screen.setup(width=1800, height=900, startx=-100, starty=-100)
set_start_position(-400, -200)
t.penup()

#movements
paint_lines(num_lines=10, num_dots=10)

#always at end
screen.exitonclick()