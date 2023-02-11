import turtle
import pandas

image = "blank_states_img.gif"
guesses = []

screen = turtle.Screen()
screen.title("US States Game")
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")


while len(guesses) < 50:

    answer_state = screen.textinput(title=f'{len(guesses)}/50 states correct',
                                    prompt="What's another state's name?").title()
    if answer_state in data.state.to_list():
        state = turtle.Turtle()
        state.hideturtle()
        state.pu()

        guesses.append(answer_state)

        state_data = data[data.state == answer_state]
        x_cor = int(state_data.x)
        y_cor = int(state_data.y)

        state.goto(x_cor, y_cor)
        state.write(f'{answer_state}', align="right")

    elif answer_state == "Exit":
        missing_states = [state for state in data.state if state not in guesses]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")

        break


screen.exitonclick()
