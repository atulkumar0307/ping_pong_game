from turtle import Turtle


class Paddle(Turtle):   # Defining the inheritance of class Turtle in class Paddle.

    def __init__(self, position):   # initialize the paddle with all this property as this class called and demanding an argument.
        super().__init__()      # Inheriting the all property of class Turtle by using super() function.
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(position)

    def go_up(self):    # Used by listen method to move paddle.
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):  # Used by listen method to move paddle.
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
