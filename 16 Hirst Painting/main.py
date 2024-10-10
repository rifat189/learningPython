# Hirst Painting

import random
import turtle
from turtle import Screen

import colorgram
colors = colorgram.extract('hirst_painting.webp', 600)
rgb_colors = []
for i in colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
# print(rgb_colors)
riff = turtle.Turtle()
turtle.colormode(255)
# riff.shape("default")
riff.penup()
riff.hideturtle()
riff.speed("fastest")
riff.setheading(225)
riff.forward(300)
riff.setheading(0)
dot_size = int(input("Enter dot size: "))
gap = dot_size + int(input("Enter gap size: "))
painting_size = int(input("Enter painting size: "))
for i in range(painting_size):
    for j in range(painting_size):
        riff.dot(dot_size, random.choice(rgb_colors))
        riff.forward(gap)
    riff.setheading(90)
    riff.forward(gap)
    riff.setheading(180)
    riff.forward(gap*painting_size)
    riff.setheading(360)

screen = Screen()
screen.exitonclick()

