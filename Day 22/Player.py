from turtle import Turtle, Screen

UP = 90
DOWN = 270


class Player(Turtle):
    def __init__(self, location, player_color):
        super().__init__(shape="square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color(player_color)
        self.goto(location)

    def move_up(self):
        new_y = self.ycor() + 35
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 35
        self.goto(self.xcor(), new_y)


