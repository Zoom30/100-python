import time
from Food import Food
from Snake import Snake
from turtle import Screen
from Scoreboard import Scoreboard

# Screen setup
screen = Screen()
screen.bgcolor("black")
screen.tracer(0)
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.listen()

snake = Snake()
food = Food()
score = Scoreboard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")

screen.onkey(snake.right, "Right")
is_playing = True
while is_playing:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision from food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.update_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.game_over()
        is_playing = False

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_playing = False
            score.game_over()


screen.mainloop()
