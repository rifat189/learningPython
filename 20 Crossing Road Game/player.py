from turtle import Turtle, Screen

# from main import screen

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0, -220)
        self.setheading(90)

    def re_position(self):
        self.goto(0, -220)
        self.setheading(90)

    def move(self):
        self.forward(20)
