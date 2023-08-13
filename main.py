import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


states = pandas.read_csv("50_states.csv")
state_pen = turtle.Turtle()
state_pen.hideturtle()
states_dict = states.to_dict()

still_guessing = True
while still_guessing:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    for num in range(0, 50):
        if answer_state == states_dict['state'][num]:
            x = states_dict['x'][num]
            y = states_dict['y'][num]
            state_pen.penup()
            state_pen.hideturtle()
            state_pen.goto(x, y)
            state_pen.write(states_dict['state'][num])
        if answer_state == "exit":
            still_guessing = False
            break
screen.exitonclick()


