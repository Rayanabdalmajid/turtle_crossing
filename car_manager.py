from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.cars = []
        self.distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        choice = random.randint(1,6)
        if choice == 6:
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.setheading(180)
            new_car.goto(300, random.randint(-250,250))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            self.cars.append(new_car)

    def moving_cars(self):
        for car in self.cars:
            car.forward(self.distance)

    def increase_speed(self):
        self.distance += MOVE_INCREMENT


