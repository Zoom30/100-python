from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.color("white")
        self.penup()
        self.goto(0, -280)

        self.hideturtle()

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.current_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.current_score += 1
        self.clear()
        self.write(arg=f"Score: {self.current_score}", align="center", font=("Arial", 15, "normal"))
