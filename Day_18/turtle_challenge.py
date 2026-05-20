######## Challenge 1 - Draw a Square ############
import turtle as t

# from turtle import Turtle, Screen
# timmy_the_turtle = Turtle()

# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)

tim = t.Turtle()

# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)


########### Challenge 2 - Draw a Dashed Line ########

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

########### Challenge 3 - Draw Shapes ########
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# for shape_side_n in range(3, 10):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)

########### Challenge 4 - Random Walk ########
t.colormode(255)
# directions = [0, 90, 180, 270]
# tim.pensize(15)
tim.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# for _ in range(100):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

########### Challenge 5 - Spirograph ########
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap) ):
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()