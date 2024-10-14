# Crossing Road Game

import random
import time
from turtle import Turtle, Screen
from player import *
from obstacle import *
from scoreboard import *

screen = Screen()
screen.setup(width=800, height=500)
screen.tracer(0)
player = Player()
obs = Obstacle()
score = Scoreboard()


screen.listen()
screen.onkey(key="Up", fun=player.move)


is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    obs.create_obstacle()
    obs.move_obstacle()

    for ob in obs.all_obstacle:
        if ob.distance(player) < 20:
            score.game_over()
            is_game_on = False

    if player.ycor() > 230:
        # is_game_on = False
        score.level_up()
        player.re_position()
        obs.move_speed_increase()


screen.exitonclick()
