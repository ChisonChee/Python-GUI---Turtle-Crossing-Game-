import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_number = []
        self.move_incrementer = 0
        self.starting_move_distance = STARTING_MOVE_DISTANCE
        self.move_increment = MOVE_INCREMENT

    def add_car(self):
        chance = random.randint(1,6)
        if chance == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(300, random.randint(-140, 240))
            new_car.seth(180)
            self.car_number.append(new_car)

    def moving_car(self):
        self.starting_move_distance += (self.move_incrementer * self.move_increment)
        for car in self.car_number:
            car.fd(self.starting_move_distance)
