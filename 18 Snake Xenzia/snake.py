from turtle import *
starting_position = [(0, 0), (-20, 0), (-40, 0)]
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
MOVE_DISTANCE = 20
HEAD_COLOR = "teal"

class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        # self.head = self.segment[0]
    def create_snake(self):
        for i in starting_position:
            self.add_segment(i)
        self.segment[0].color(HEAD_COLOR)
        # self.segment[0].forward(20)
    def add_segment(self, position):
        new_segment = Turtle()
        new_segment.penup()
        new_segment.shape("square")
        new_segment.goto(position)
        self.segment.append(new_segment)

    def extend(self):
        last_segment_position = self.segment[-1].position()
        self.add_segment(last_segment_position)

    def move_snake(self):
        for i in range(len(self.segment)-1, 0 , -1):
            new_x = self.segment[i-1].xcor()
            new_y = self.segment[i-1].ycor()
            self.segment[i].goto(new_x, new_y)
            # print(self.segment[i].xcor(), self.segment[i].ycor())
        self.segment[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segment[0].heading() != DOWN:
            self.segment[0].setheading(UP)
    def down(self):
        if self.segment[0].heading() != UP:
            self.segment[0].setheading(DOWN)
    def right(self):
        if self.segment[0].heading() != LEFT:
            self.segment[0].setheading(RIGHT)
    def left(self):
        if self.segment[0].heading() != RIGHT:
            self.segment[0].setheading(LEFT)