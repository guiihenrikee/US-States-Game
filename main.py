import turtle
import pandas
from turtle import Turtle
screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()    #states  to a list

cord_x = data["x"].to_list()
cord_y = data["y"].to_list()
cord = []
for cor in range(len(states_list)):    #cordinates to a list of tuples
    current = (cord_x[cor], cord_y[cor])
    cord.append(current)

writer = Turtle()    #to display the states name
writer.hideturtle()
writer.penup()

correct_guesses = []
score = 0
game_is_on = True

while game_is_on: #keep asking for a input till the game ends
    answer_state = screen.textinput(title=f"Guess the State {score}/50", prompt="What's another state's name").title()
    if answer_state == "Exit":
        game_is_on = False
        missing_states = []
        for i in states_list:
            if i not in correct_guesses:
                missing_states.append(i)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")   #save all missed stated in a .csv file
        break
    for states in states_list:
        if score >= 50:
            game_is_on = False
        elif answer_state == states:
            correct_guesses.append(states)
            score += 1
            index = states_list.index(answer_state)
            writer.goto(cord[index])
            writer.write(answer_state)

turtle.mainloop()
