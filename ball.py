from turtle import Turtle


class Ball(Turtle):

    def __init__(self):     # initialize the ball with all this property as this class called.
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):     # Used to move the ball.
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):     # Used to bounce the ball if ball hit in upper and lower wall / bounce from y-axis.
        self.y_move *= -1

    def bounce_x(self):     # Used to bounce the ball if ball hit the paddles  / bounce from x-axis.
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):   # Resetting the position of ball in center if any paddle miss the ball and changing position in opposite side.
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
