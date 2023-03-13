from turtle import Turtle


class ScoreBoard(Turtle):
    # constructor of the class
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(0, 250)
        self.write(f"Scores: {self.score1} - {self.score2}", True, align="center", font=('Arial', 15, 'normal'))

    def update(self):
        """
        this function update the scoreboard
        :return:
        """
        self.clear()
        self.setposition(0, 250)
        self.write(f"Scores: {self.score1} - {self.score2}", True, align="center", font=('Arial', 15, 'normal'))