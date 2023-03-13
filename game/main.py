# initial imports
from turtle import Turtle, Screen
from board import Board
import time
from ball import Ball
from scoreboard import ScoreBoard

# screen part
main_screen = Screen()
main_screen.bgcolor("black")
main_screen.title("Pong")
main_screen.setup(800, 600)
main_screen.tracer(0)

# scoreboard, and other prints on screen
score = ScoreBoard()
winner = Turtle()
winner.hideturtle()
winner.color("white")

# board part
player_1 = Board(350)
player_2 = Board(-350)

# ball part
ball = Ball()

# listeners
# player 1
main_screen.onkey(player_1.move_up, "Up")
main_screen.onkey(player_1.move_down, "Down")

# player 2
main_screen.onkey(player_2.move_up, "w")
main_screen.onkey(player_2.move_down, "s")

main_screen.listen()

# game instances
game_on = True

while game_on:
    # updating screen
    main_screen.update()
    time.sleep(0.1)

    # collision of ball with boards
    player_1.collide(ball)
    player_2.collide(ball)

    # ball collision with sides
    if 300 < ball.ycor():
        ball.bounce("upper-side")
    elif ball.ycor() < -300:
        ball.bounce("lower-side")

    # score part
    if ball.xcor() < -400:
        ball.score()
        score.score1 += 1
        score.update()

    elif ball.xcor() > 400:
        ball.score()
        score.score2 += 1
        score.update()

    # scoreboard part
    if score.score1 == 5:
        game_on = False
        winner.write("Player 1 win the game!!!", font=('Arial', 15, 'normal'))
    elif score.score2 == 5:
        game_on = False
        winner.write("Player 2 win the game!!!", font=('Arial', 15, 'normal'))

    # move of ball
    ball.move()

# last part
main_screen.listen()
main_screen.exitonclick()