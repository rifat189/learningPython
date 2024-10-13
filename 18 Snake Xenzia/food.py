import random
from turtle import *
FOOD_RANGE = 220
FOOD_COLOR = 'red'


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(FOOD_COLOR)
        self.penup()
        self.refresh()

    def refresh(self):
        random_x = random.randint(-FOOD_RANGE, FOOD_RANGE)
        random_y = random.randint(-FOOD_RANGE, FOOD_RANGE)
        self.goto(random_x, random_y)
