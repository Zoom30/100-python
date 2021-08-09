import random
from turtle import Turtle, Screen

# dan = Turtle()
screen = Screen()
# screen.listen()
#
#
# def move_forwards():
#     dan.forward(10)
#
#
# def move_backwards():
#     dan.back(10)
#
#
# def turn_right():
#     dan.right(15)
#
#
# def turn_left():
#     dan.left(15)
#
#
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="d", fun=turn_right)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="c", fun=dan.clear)
#


# ===========================================================================

# timmy = Turtle()
# tommy = Turtle()
#
# timmy.color("blue")
# tommy.color("purple")
#
# timmy.forward(10)
# tommy.penup()
# tommy.goto(0, screen.canvheight - 1)
# tommy.forward(20)

# ===============================================================================
timmy = Turtle()
tommy = Turtle()
jimmy = Turtle()
johnny = Turtle()
kenny = Turtle()
gabi = Turtle()
turtles = [timmy, tommy, jimmy, johnny, kenny, gabi]
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
color_choice = 0
for turtle in turtles:
    turtle.shape("turtle")
    turtle.penup()
    turtle.color(colors[color_choice])
    color_choice += 1

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race? Enter a color ({colors}): ")
print(user_bet)


def go_to_start_position(turtle_list):
    y_value = -100
    for _turtle in turtle_list:
        _turtle.goto(x=-230, y=y_value)
        y_value += 50


def start_race():
    finish_line = screen.canvwidth / 2
    print(f"finish line is at {finish_line}")
    random_speed = ["fastest", "fast", "normal", "slow", "slowest"]
    random_distance = [4, 8, 12, 16, 20]
    is_racing = True
    while is_racing:
        for racing_turtle in turtles:
            racing_turtle.forward(random.choice(random_distance))
            # racing_turtle.speed(random.choice(random_speed))
            print(racing_turtle.xcor())
            if racing_turtle.xcor() >= finish_line:
                winner_color = racing_turtle.color()[0]
                print(f"{winner_color} has won")
                if user_bet == winner_color:
                    print("You won your bet")
                else:
                    print("You lost your bet")
                is_racing = False
                break


go_to_start_position(turtles)
start_race()
screen.exitonclick()
