from turtle import Turtle
ALIGNMENT = "center"
FONT = ("arial", 12, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("black")
        self.penup()
        self.goto(50, 220)
        self.write(f"{self.r_score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.goto(-50, 220)
        self.write(f"{self.l_score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.goto(50, 220)
        self.write(f"{self.r_score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.goto(-50, 220)
        self.write(f"{self.l_score}", align=ALIGNMENT, font=FONT)

    def l_score_update(self):
        self.l_score += 1
        self.update_score()

    def r_score_update(self):
        self.r_score += 1
        self.update_score()