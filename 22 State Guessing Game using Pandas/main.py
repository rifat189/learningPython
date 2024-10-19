# State Guessing Game

import turtle
# from turtle import Turtle, Screen
import pandas

screen = turtle.Screen()
screen.setup(width=800, height= 600)
screen.title("Guessing the states")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_data = pandas.read_csv("50_states.csv")
all_states = state_data.state.to_list()
print(all_states)
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"({len(guessed_state)}/50) State Name",
                                    prompt="Guess a new state").title()
    if answer_state == 'Exit':
        missing_states = []
        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
        df = pandas.DataFrame(missing_states)
        df.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        current_state = state_data[state_data.state == answer_state]
        t.goto(int(current_state.x.iloc[0]), int(current_state.y.iloc[0]))
        t.write(answer_state)

# screen.mainloop()
