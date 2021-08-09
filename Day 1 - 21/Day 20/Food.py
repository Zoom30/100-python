from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.75, stretch_len=0.75)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x_cor = random.randint(-280, 280)
        random_y_cor = random.randint(-280, 280)
        self.goto(random_x_cor, random_y_cor)
