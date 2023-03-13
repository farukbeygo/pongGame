from turtle import Turtle
from random import randint


class Ball(Turtle):
    # constructor of the class
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.xpeed = 15
        self.ypeed = 15

    def move(self):
        """
        this function move the ball
        :return:
        """
        x = self.xcor() + self.xpeed
        y = self.ycor() + self.ypeed
        self.goto(x, y)

    def bounce(self, side):
        """
        this function detect the collision of the ball with side of the screen
        :param side:
        :return:
        """
        if side == "upper-side":
            self.ypeed = -self.ypeed
        else:
            self.ypeed = -self.ypeed

    def collide(self):
        """
        this function change the direction of the ball when collide with boards
        :return:
        """
        self.xpeed = -self.xpeed

    def score(self):
        """
        this function restart the game when player scored
        :return:
        """
        self.goto(0, 0)
        self.xpeed = -self.xpeed
        self.ypeed = -self.ypeed


