from turtle import Turtle, Screen


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.goto(position)
        self.shapesize(stretch_wid=5, stretch_len=1, outline=None)

    def go_up(self):
        self.goto(x=self.xcor(), y=(self.ycor()+20))

    def go_down(self):
        self.goto(x=self.xcor(), y=(self.ycor()-20))

