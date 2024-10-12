import random
import turtle
from turtle import *

screen = Screen()
screen.setup(width=500, height=400)
colors = ['green', 'blue', 'red']
user_bet = turtle.textinput(title="Place your bet", prompt="Who will win the race: ")
y_position = [30, 0, -30]
ninja_turtles = []

for i in range(0, 3):
    new_turtle = turtle.Turtle()
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(-230, y_position[i])
    ninja_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for t in ninja_turtles:
        if t.xcor() > 230:
            is_race_on = False
            winning_color = t.pencolor()
            if winning_color == user_bet:
                print(f"You've won!! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost!! The {winning_color} turtle is the winner")
        random_distance = random.randint(0, 30)
        t.forward(random_distance)

screen.exitonclick()
