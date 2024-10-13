from turtle import Turtle

BALL_SPEED_INCREMENT = 0.9

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("teal")
        self.penup()
        self.goto(0, 0)
        self.x_speed = 10
        self.y_speed = 10
        self.ball_speed = 0.1

    def move_ball(self):
        new_x = self.xcor() + self.x_speed
        new_y = self.ycor() + self.y_speed
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_speed *= -1
        self.ball_speed *= BALL_SPEED_INCREMENT
        self.move_ball()

    def bounce_x(self):
        self.x_speed *= -1
        self.ball_speed *= BALL_SPEED_INCREMENT
        self.move_ball()

    def game_reset(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.bounce_x()

