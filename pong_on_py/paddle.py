from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(5,1)
        self.penup()
        self.goto(position)
    
    def move_up(self):
        self.newy = self.ycor() + 20
        self.goto(self.xcor(),self.newy)
    
    def move_down(self):
        self.newy = self.ycor() - 20
        self.goto(self.xcor(), self.newy)
    