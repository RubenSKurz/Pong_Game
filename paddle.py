from turtle import Turtle
X_POS = [350, -350]
Y_POS = [0, 0]
WIDTH = 1
HEIGHT = 5


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.setheading(90)
        self.color("white")
        self.turtlesize(stretch_wid=WIDTH, stretch_len=HEIGHT, outline=1)

    def start_position(self, number):
        self.goto(x=X_POS[number], y=Y_POS[number])

    def paddle_up(self):
        if not self.ycor() >= 250:
            self.forward(25)

    def paddle_down(self):
        if not self.ycor() <= -250:
            self.backward(25)
