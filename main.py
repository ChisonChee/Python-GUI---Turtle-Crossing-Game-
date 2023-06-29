import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "w".lower())

i = 0
j = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.add_car()

    if player.ycor() == 280:
        player.reset_position()
        scoreboard.scores()
        car.move_incrementer = 1

    for cars in car.car_number:
        if cars.distance(player) < 20:
            scoreboard.end_game()
            game_is_on = False

    car.moving_car()
    car.move_incrementer = 0

screen.exitonclick()
