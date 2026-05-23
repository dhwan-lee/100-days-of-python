import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.move_up, "Up")

car_manager = CarManager()

scoreboard = Scoreboard()
scoreboard.increase_level()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_cars()
    car_manager.move()

    # Detect successful crossing
    if player.ycor() > 280:
        player.reset_position()
        scoreboard.increase_level()
        car_manager.speed_up()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()