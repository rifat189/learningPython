from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.color("black")
        self.penup()
        self.goto(-350, 210)
        self.hideturtle()
        self.write(f"Level: {self.level}", align = 'center', font=('arial', 16, 'normal'))

    def level_up(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align = 'center', font=('arial', 16, 'normal'))
