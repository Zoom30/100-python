from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.setup(width=725, height=491)
screen.bgpic("blank_states_img.gif")

turtle = Turtle(shape="turtle")
turtle.penup()
turtle.hideturtle()

data = pandas.read_csv("50_states.csv")
data_states = data["state"]
state_names = data_states.to_list()
x = 0
for state_name in state_names:
    state_names[x] = state_name.lower()
    x += 1

df = data[["x", "y"]]
df_dict_version = df.to_dict()
position = []
for x in range(len(state_names)):
    position.append((df_dict_version["x"][x], df_dict_version["y"][x]))

list_of_dict = []

for x in range(len(state_names)):
    entry = {
        "State": state_names[x],
        "Location": position[x]
    }
    list_of_dict.append(entry)

number_of_states = len(state_names)
correctly_guessed = 0
guessed_states = []
states_to_learn_ver2 = [item for item in state_names if not item in guessed_states]
states_to_learn = []
while correctly_guessed <= number_of_states:
    user_guess = screen.textinput(title=f"Guess! {correctly_guessed} / {number_of_states} Correct", prompt="Guess the "
                                                                                                           "states: "
                                                                                                           "").lower()
    for x in range(number_of_states):
        if list_of_dict[x]["State"] == user_guess:
            turtle.goto(list_of_dict[x]["Location"])
            turtle.write(user_guess.title(), align="center", font=("Arial", 10, "bold"))
            guessed_states.append(user_guess)
            state_names.pop(state_names.index(user_guess))
            correctly_guessed += 1
    if user_guess == "exit":
        states_to_learn_ver2 = [item for item in state_names if not item in guessed_states]
        new_data = pandas.DataFrame(states_to_learn_ver2)
        new_data.to_csv("states_to_learn_ver2.csv")
        break

# screen.mainloop()
