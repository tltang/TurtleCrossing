from turtle import Turtle
import random

FONT = ("Courier", 24, "normal")

ALIGNMENT = "Center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("black")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.speed("fastest")
        self.score_total = 0
        self.goto(-200, 260)
        self.hideturtle()
        self.score()

    def score(self):
        self.score_total += 1
        display_text = "Level: " + str(self.score_total)
        self.clear()
        self.write(display_text, move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        display_text = "GAME OVER!"
        self.color("red")
        self.home()
        self.write(display_text, move=False, align="center", font=('Arial', 12, 'bold'))
