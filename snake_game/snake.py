from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake = []
        self.init_snake()
        self.head = self.snake[0]

    def init_snake(self):
        x_pos = 0
        y_pos = 0
        for i in range(3):
            self.add_segment((x_pos, y_pos))
            x_pos -= MOVE_DISTANCE
        self.head = self.snake[0]

    def add_segment(self, position):
        new_snake = Turtle("square")
        new_snake.color("SpringGreen")
        new_snake.penup()
        new_snake.goto(position)
        self.snake.append(new_snake)

    def reset(self):
        for segment in self.snake:
            segment.goto(1000,1000)
        self.snake.clear()
        self.init_snake()

    def move(self):
        for segment in range(len(self.snake) - 1, 0, -1):
            self.snake[segment].goto(self.snake[segment - 1].position())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def grow(self):
        self.add_segment(self.snake[-1].position())
