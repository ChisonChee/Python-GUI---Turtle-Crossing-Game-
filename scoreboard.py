from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-280, 260)
        self.the_score = 1
        self.write(f"Level: {self.the_score}", align="left", font=FONT)

    def scores(self):
        self.clear()
        self.the_score += 1
        self.write(f"Level: {self.the_score}", align="left", font=FONT)

    def end_game(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="Center", font=FONT)
