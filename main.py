import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    car_manager.create_car()
    car_manager.moving_cars()

    for car in car_manager.cars:
        if car.distance(player) < 25:
            game_is_on = False
            score_board.game_over()

    if player.is_on_the_finish_line():
        player.start_over()
        car_manager.increase_speed()
        score_board.level_up()

screen.exitonclick()

