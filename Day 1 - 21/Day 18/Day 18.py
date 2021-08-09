import math
import random
from turtle import Turtle, Screen
import colorgram

timmy_turtle = Turtle(visible=False)
timmy_turtle.shape("turtle")
timmy_turtle.color("green")
screen = Screen()
# screen.colormode(255)

# def draw_square(size):
#     start_point_x = -1 * (size / 2)
#     start_point_y = size / 2
#     timmy_turtle.penup()
#     timmy_turtle.goto(start_point_x, start_point_y)
#     timmy_turtle.pendown()
#     timmy_turtle.showturtle()
#
#     for x in range(0, 4):
#         timmy_turtle.forward(size)
#         timmy_turtle.right(90)

# ============================================================

# def draw_broken_lines(size):
#     start_point_x = float(-screen.canvwidth)
#     timmy_turtle.penup()
#     timmy_turtle.goto(start_point_x, 0)
#     timmy_turtle.pendown()
#     for x in range(size):
#         timmy_turtle.showturtle()
#         timmy_turtle.forward(10)
#         timmy_turtle.penup()
#         timmy_turtle.forward(10)
#         timmy_turtle.pendown()

# ============================================================

# def draw_polygons(size):
#     start_point_y = float(screen.window_height() / 2)
#     start_point_x = -1 * (size / 2)
#     timmy_turtle.penup()
#     timmy_turtle.goto(x=start_point_x, y=start_point_y)
#     timmy_turtle.pendown()
#     timmy_turtle.showturtle()
#     no_of_sides = 3
#     #timmy_turtle.speed("fastest")
#
#     while no_of_sides < 1000:
#         interior_angle = 180 - ((no_of_sides - 2) * 180) / no_of_sides
#         red_value = random.randint(1, 255)
#         green_value = random.randint(1, 255)
#         blue_value = random.randint(1, 255)
#         for _ in range(no_of_sides):
#             screen.colormode(255)
#             timmy_turtle.color(red_value, green_value, blue_value)
#             timmy_turtle.forward(size)
#             timmy_turtle.right(interior_angle)
#         no_of_sides += 1


# ====================================================================================================


# def random_walk(distance):
#     timmy_turtle.showturtle()
#     timmy_turtle.pensize(10)
#
#     for _ in range(250):
#         screen.colormode(255)
#         red_value = random.randint(1, 255)
#         green_value = random.randint(1, 255)
#         blue_value = random.randint(1, 255)
#         timmy_turtle.color(red_value, green_value, blue_value)
#         x = random.randint(1, 4)
#         if x == 1:
#             timmy_turtle.forward(distance)
#         elif x == 2:
#             timmy_turtle.right(90)
#             timmy_turtle.forward(distance)
#         elif x == 3:
#             timmy_turtle.back(distance)
#         else:
#             timmy_turtle.left(90)
#             timmy_turtle.forward(distance)
# =============================================================================================

# Angela's Method

# def random_walk(distance):
#     directions = [0, 90, 180, 270]
#     timmy_turtle.speed("fastest")
#     no_of_walks = 0
#     for _ in range(200):
#
#         red_value = random.randint(1, 255)
#         green_value = random.randint(1, 255)
#         blue_value = random.randint(1, 255)
#         timmy_turtle.showturtle()
#         timmy_turtle.pensize(10)
#         timmy_turtle.color(red_value, green_value, blue_value)
#         timmy_turtle.forward(distance)
#         timmy_turtle.seth(random.choice(directions))
#         no_of_walks += 1
#         print(f"Turtle walked {no_of_walks} times")

# ====================================================================================================

def draw_spirograph(radius, gap):
    timmy_turtle.pensize(2)
    for _ in range(int(math.ceil(360 / gap))):
        screen.colormode(255)
        red_value = random.randint(1, 255)
        green_value = random.randint(1, 255)
        blue_value = random.randint(1, 255)
        timmy_turtle.speed("fastest")
        timmy_turtle.color(red_value, green_value, blue_value)
        timmy_turtle.circle(radius, steps=1000)

        timmy_turtle.left(gap)

# ====================================================================================================

# Angela's version
# def draw_spirograph_angelas(radius, size_of_the_gap):
#     timmy_turtle.speed("fastest")
#     for _ in range(int(360 / size_of_the_gap)):
#         red_value = random.randint(1, 255)
#         green_value = random.randint(1, 255)
#         blue_value = random.randint(1, 255)
#         timmy_turtle.color(red_value, green_value, blue_value)
#         timmy_turtle.circle(radius)
#         timmy_turtle.seth(timmy_turtle.heading() + size_of_the_gap)


# ====================================================================================================

# Daniel's painting

# add an image to the directory to extract colors
colors = colorgram.extract("IMG-20150519-WA0006.jpg", 30)

color_choices = []
for color in colors:
    color_choices.append(color.rgb)


def draw_daniels_painting():
    timmy_turtle.speed("fastest")
    timmy_turtle.showturtle()
    timmy_turtle.pensize(15)
    timmy_turtle.penup()

    drawing_start_point_x = -1 * screen.canvwidth
    drawing_start_point_y = -1 * screen.canvheight

    timmy_turtle.goto(drawing_start_point_x, drawing_start_point_y)

    height = 0
    print(timmy_turtle.xcor())
    while height < 475:
        for _ in range(25):
            screen.colormode(255)
            random_color = random.choice(color_choices)
            timmy_turtle.color(random_color.r, random_color.g, random_color.b)
            timmy_turtle.pendown()
            timmy_turtle.forward(1)
            timmy_turtle.penup()
            timmy_turtle.forward(25)
            print(timmy_turtle.xcor())

        height += 19
        timmy_turtle.goto(drawing_start_point_x, drawing_start_point_y + height)

# ====================================================================================

# Angela's Method

# def draw_daniels_painting_angela():
#     timmy_turtle.showturtle()
#     timmy_turtle.speed("fastest")
#     rgb_colors = []
#     colors_angela = colorgram.extract("IMG-20150519-WA0006.jpg", 30)
#     screen.colormode(255)
#     for color_angela in colors_angela:
#         r = color_angela.rgb.r
#         g = color_angela.rgb.g
#         b = color_angela.rgb.b
#         new_color = (r, g, b)
#         rgb_colors.append(new_color)
#     timmy_turtle.penup()
#     timmy_turtle.hideturtle()
#     timmy_turtle.setheading(225)
#     timmy_turtle.forward(300)
#     timmy_turtle.setheading(0)
#
#     number_of_dots = 100
#     for dot_count in range(1, number_of_dots + 1):
#         timmy_turtle.dot(20, (random.choice(rgb_colors)))
#
#         timmy_turtle.forward(50)
#
#         if dot_count % 10 == 0:
#             timmy_turtle.setheading(90)
#             timmy_turtle.forward(50)
#             timmy_turtle.setheading(180)
#             timmy_turtle.forward(500)
#             timmy_turtle.setheading(0)
#
#
#     print(rgb_colors)


draw_daniels_painting()
# draw_daniels_painting_angela()

# draw_square(400)
# draw_broken_lines(300)
# draw_polygons(60)
# random_walk(30)
# draw_spirograph(100, 5)

screen.exitonclick()
