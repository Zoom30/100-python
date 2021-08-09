from turtle import Turtle, Screen

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.current_heading = 0

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for body in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[body - 1].xcor()
            new_y = self.segments[body - 1].ycor()
            self.segments[body].goto(x=new_x, y=new_y)
            self.current_heading = self.head.heading()
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if not self.current_heading == DOWN:
            self.head.setheading(UP)

    def down(self):
        if not self.current_heading == UP:
            self.head.setheading(DOWN)

    def left(self):
        if not self.current_heading == RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if not self.current_heading == LEFT:
            self.head.setheading(RIGHT)
