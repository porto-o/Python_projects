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
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    player.detect_final()

    car.create_car()
    car.move_cars()

    for item in car.all_cars:
        if item.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.detect_final():
        player.set_start()
        car.level_up()
        scoreboard.increase()

screen.exitonclick()
