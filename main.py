import pandas
import turtle

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()


screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

missing_states = []
guessed_state = []
while len(guessed_state) <= 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50",prompt="Guess the state").title()

    if answer_state == "Exit":
        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("StatestoLearn.csv")
        break
        
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_state)
        guessed_state.append(answer_state)
