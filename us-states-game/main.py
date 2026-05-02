from write import Write
import turtle
import pandas as pd

"""
Screen Setup
"""
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width=725, height=500)

"""
CSV Setup
"""
data = pd.read_csv("50_states.csv")

"""
Game Setup
"""
state_counter = 0
writer = Write()
guessed_states = []

while state_counter < len(data):
    answer_state = screen.textinput(
        title=f"{state_counter}/50 States Correct", prompt="Whats another state's name?").title()
    state_info = data[data.state == answer_state]

    if answer_state == "Exit":
        all_states = data.state.to_list()
        states_to_learn = []
        for state in all_states:
            if state not in guessed_states:
                states_to_learn.append(state)
        pd.DataFrame(states_to_learn, columns=["State"]).to_csv("States-to-learn.csv", index=False)

    if not state_info.empty and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_name = state_info.iat[0, 0]
        state_x = state_info.iat[0, 1]
        state_y = state_info.iat[0, 2]
        writer.write_state(state_name, state_x, state_y)
        state_counter += 1

turtle.mainloop()