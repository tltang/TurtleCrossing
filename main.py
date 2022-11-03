import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
my_player = Player()
my_score = Scoreboard()

screen.listen()
screen.onkey(my_player.up, "Up")
cars = []
i1 = 0
game_is_on = True

while game_is_on:
    i1 += 1
    if i1 == 1 or i1 % 3 == 0:
        new_car = CarManager()
        cars.append(new_car)
    for car in cars:
        if my_player.distance(car) < 20:
            game_is_on = False
            my_score.game_over()
        else:
            car.move_forward()
            # if car.xcor() < -280:
            #     cars.remove(car)
    time.sleep(0.5)
    screen.update()
    if my_player.ycor() >= 280:
        my_score.score()
        my_player.backhome()
        for car in cars:
            car.level_up()


screen.exitonclick()

