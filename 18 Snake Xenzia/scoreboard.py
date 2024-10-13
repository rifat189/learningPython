from turtle import Turtle
ALIGNMENT = "center"
FONT = ("arial", 16, "bold")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("teal")
        self.penup()
        self.goto(0, 225)
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)
