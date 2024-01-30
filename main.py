from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Screen Setup
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("THE PONG GAME!")
screen.tracer(0)    # it controls animation and to turn it off use argument 0.


# Creating paddles with argument for position at which we want to make.
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()       # Creating ball by making a ball object from class Ball.
scoreboard = Scoreboard()       # Creating a scoreboard by making an object scoreboard from class Scoreboard.


# Moving the paddles by keys using listen method from Screen class.
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


# Making a loop condition to make the game continue.
is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)     # Changing the speed of ball by using sleep method from time function and using ball class and its method move_speed as argument.
    screen.update()     # we have turned off the trace so, we have to manually updates the screen.
    ball.move()     # Making ball move.

    # Detect collision with wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()     # Making ball bounce.

    # Detect collision with paddle.
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:   # Detect collision with paddle.
        ball.bounce_x()     # Making ball bounce.

    # Detect R_paddle misses.
    if ball.xcor() > 380:
        ball.reset_position()   # After collision making the ball in center and moving in the opposite direction.
        scoreboard.l_point()

    # Detect L_paddle misses.
    if ball.xcor() < -380:
        ball.reset_position()   # After collision making the ball in center and moving in the opposite direction.
        scoreboard.r_point()

screen.exitonclick()
