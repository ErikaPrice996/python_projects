import time
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake

WAIT_TIME = 0.1


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake? Snake??? SNAAAAAKE!!!")
screen.tracer(0)

def update_snake():
    screen.update()
    time.sleep(WAIT_TIME)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    update_snake()
    snake.move()

    #food has been touched by snake
    if snake.head.distance(food) < 15:
        food.move()
        scoreboard.update_score()
        snake.grow()

    #collided with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() >280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        # original version of game
        # game_on = False
        # scoreboard.game_over()

    #detect collision with self
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            # original version of game
            # game_on = False
            # scoreboard.game_over()



screen.exitonclick()