# initial imports
from turtle import Turtle
from ball import Ball


# board class
class Board:
    # constructor of the class
    def __init__(self, position):
        self.board = Turtle("square")
        self.board.shapesize(5, 1)
        self.board.color("white")
        self.board.penup()
        self.board.goto(position, 0)

    def move_up(self):
        """
        this function increase the y-cor of boards
        :return:
        """
        initial_x = self.board.xcor()
        initial_y = self.board.ycor()
        self.board.goto(initial_x, initial_y + 30)

    def move_down(self):
        """
        this function decrease the y-cor of boards
        :return:
        """
        initial_x = self.board.xcor()
        initial_y = self.board.ycor()
        self.board.goto(initial_x, initial_y - 30)

    def collide(self, ball):
        """
        this function take a parameter from ball class and detect collision of the ball with the boards
        :param ball:
        :return:
        """
        if abs(self.board.xcor() - ball.xcor()) < 10 and abs(self.board.ycor() - ball.ycor()) < 50:
            ball.collide()








