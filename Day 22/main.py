from Player import Player
from turtle import Screen
from Ball import *
import time
from Scoreboard import Scoreboard

# Screen Set-Up
new_screen = Screen()
new_screen.title("Pong")
new_screen.bgcolor("black")
new_screen.setup(800, 600)
new_screen.listen()
# new_screen.tracer(0)

# Player Set-Up
player_1 = Player(location=(350, 0), player_color="yellow")
player_2 = Player(location=(-350, 0), player_color="red")

# Keys Set-Up
new_screen.onkey(fun=player_1.move_up, key="Up")
new_screen.onkey(fun=player_1.move_down, key="Down")
new_screen.onkey(fun=player_2.move_up, key="w")
new_screen.onkey(fun=player_2.move_down, key="s")

# Ball Set-Up
ball = Ball()

# Scoreboard Set-Up
scoreboard = Scoreboard()


is_playing = True
while is_playing:
    time.sleep(ball.move_speed)
    new_screen.update()
    ball.move_ball()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y_axis()

    if ball.distance(player_1) < 50 and ball.xcor() > 320 or ball.distance(player_2) < 50 and ball.xcor() < -320:
        ball.bounce_x_axis()

    if ball.xcor() > 400:
        scoreboard.player_2_point()
        time.sleep(0.5)
        ball.reset_position()

    if ball.xcor() < -400:
        scoreboard.player_1_point()
        time.sleep(0.5)
        ball.reset_position()

new_screen.mainloop()
