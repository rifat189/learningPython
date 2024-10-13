from turtle import *

PADDLE_SPEED_INCREMENT = 25

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("black")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up(self):
        self.goto(self.xcor(), self.ycor() + PADDLE_SPEED_INCREMENT)
    def down(self):
        self.goto(self.xcor(), self.ycor() - PADDLE_SPEED_INCREMENT)


