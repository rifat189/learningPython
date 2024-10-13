# Ping Pong Arcade Game

import time
from turtle import Turtle, Screen
from paddle import *
from ball import *
from scoreboard import Score


screen = Screen()
screen.setup(width=800, height=500)
screen.tracer(0)

right_paddle = Paddle((380, 0))
left_paddle = Paddle((-380, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(key='Up', fun=right_paddle.up)
screen.onkey(key='Down', fun=right_paddle.down)
screen.onkey(key='w', fun=left_paddle.up)
screen.onkey(key='s', fun=left_paddle.down)

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move_ball()

    if ball.ycor()>240 or ball.ycor()<-240:
        ball.bounce_y()

    if ball.xcor()>360 and ball.distance(right_paddle)<70 or ball.xcor()<-360 and ball.distance(left_paddle)<70:
        ball.bounce_x()


    if ball.xcor()>360 and not ball.distance(right_paddle)<70:
        ball.game_reset()
        score.l_score_update()

    if ball.xcor() < -360 and not ball.distance(left_paddle)<70:
        ball.game_reset()
        score.r_score_update()




screen.exitonclick()
