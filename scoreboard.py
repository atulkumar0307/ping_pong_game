from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):     # initialize the scoreboard with all this property as this class called.
        super().__init__()
        self.color("red")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):    # Used to update the scoreboard and can use while initialize the class Scoreboard.
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 60, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 60, "normal"))

    def l_point(self):      # Increasing the score of l_paddle as r_paddle misses the ball and update scoreboard.
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):      # Increasing the score of r_paddle as l_paddle misses the ball and update scoreboard.
        self.r_score += 1
        self.update_scoreboard()
