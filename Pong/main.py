import time
from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

POSITIONS = [(350, 0), (-350, 0)]
MATCH_POINT = 3

#Screen Setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

#scoreboard setup
left_score = Scoreboard((-100, 200))
right_score = Scoreboard((100, 200))

#create paddles
right_paddle = Paddle(POSITIONS[0])
left_paddle = Paddle(POSITIONS[1])
ball = Ball()

#Paddle Movements
screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

def screen_update():
    screen.update()
    time.sleep(ball.ball_speed)


#game play
game_active = True

while game_active:
    screen_update()
    ball.move()
    ball.detect_collision_border()

    #paddle collisions
    if ball.distance(right_paddle) < 55.0 and ball.xcor() > 325:
        if ball.heading() < 90.0:
            ball.setheading(180 - ball.heading())
        else:
            angle = 360 - ball.heading()
            deflection = 180 - angle * 2
            ball.setheading(ball.heading() - deflection)
        ball.increase_speed()

    if ball.distance(left_paddle) < 55 and ball.xcor() < -325:
        angle = 180 - ball.heading()
        # this makes no sense mathematically, but it works because if angle
        # is negative it's just doubling the negative amount
        deflection = 180 - angle * 2
        ball.setheading(ball.heading() - deflection)
        ball.increase_speed()

    if ball.detect_point_scored():
        if ball.xcor() > 1:
            right_score.update_score()
        else:
            left_score.update_score()
        ball.reset()

    if right_score.score > MATCH_POINT or left_score.score > MATCH_POINT:
        right_score.game_over()
        game_active = False




screen.exitonclick()