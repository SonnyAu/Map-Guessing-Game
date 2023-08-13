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

guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?")
    if answer_state.title() == "Exit":
        missing_states = []
        for state in states_dict['state'].values():
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    for num in range(0, 50):
        if answer_state.title() == states_dict['state'][num].title():
            guessed_states.append(answer_state)
            x = states_dict['x'][num]
            y = states_dict['y'][num]
            state_pen.penup()
            state_pen.hideturtle()
            state_pen.goto(x, y)
            state_pen.write(states_dict['state'][num])




