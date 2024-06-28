import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = ScoreBoard()

screen.listen()
screen.onkey(fun=player.go_up, key="Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            score.game_over()
            game_is_on = False

    if player.is_at_finish_line():
        score.increase_level()
        car_manager.increase_speed()
        player.go_to_start()

screen.exitonclick()