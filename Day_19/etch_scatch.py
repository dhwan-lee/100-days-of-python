import turtle as t

tim = t.Turtle()


def forward():
    tim.forward(10)

def backward():
    tim.backward(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def counterclockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

screen = t.Screen()
screen.onkey(forward, "w")
screen.onkey(backward, "s")
screen.onkey(counterclockwise, "a")
screen.onkey(clockwise, "d")
screen.onkey(clear, "c")
screen.listen()
screen.exitonclick()
