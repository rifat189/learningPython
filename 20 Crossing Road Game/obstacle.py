import random
import time
from turtle import *

MOVE_INCREMENT = 10
COLORS = ['darksalmon', 'navy', 'darkgoldenrod1', 'lightblue4', 'aquamarine4']

class Obstacle:
    def __init__(self):
        self.all_obstacle = []

    def create_obstacle(self):
        if random.randint(1, 6)==1:
            new_obstacle = Turtle()
            new_obstacle.shape("square")
            new_obstacle.color(random.choice(COLORS))
            new_obstacle.penup()
            new_obstacle.shapesize(stretch_wid=1, stretch_len=2)
            self.random_x = random.randint(400, 420)
            self.random_y = random.randint(-180, 200)
            new_obstacle.goto(self.random_x, self.random_y)
            self.all_obstacle.append(new_obstacle)

    def move_obstacle(self):
        for ob in self.all_obstacle:
            ob.backward(MOVE_INCREMENT)

    def move_speed_increase(self):
        global  MOVE_INCREMENT
        MOVE_INCREMENT += 5