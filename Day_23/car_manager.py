import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        rand_chance = random.randint(1, 6)

        if rand_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            new_car.speed = STARTING_MOVE_DISTANCE
            new_car.rand_ycor = random.randint(-250, 250)
            new_car.goto(300, new_car.rand_ycor)
            self.all_cars.append(new_car)

     
    def move(self):
        for car in self.all_cars:
            car.forward(self.speed)

    def speed_up(self):
        self.speed += MOVE_INCREMENT