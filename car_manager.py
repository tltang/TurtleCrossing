from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
YCOL = [-220, -180, -140, -100, -60, -20, 20, 60, 100, 140, 180, 220, 260]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1,stretch_len=2,outline=1)
        self.car_speed = STARTING_MOVE_DISTANCE
        self.color(random.choice(COLORS))
        self.penup()
        self.setheading(180)
        self.goto(280, random.choice(YCOL))

    def move_forward(self):
        self.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
