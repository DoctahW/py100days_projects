from turtle import Turtle



class Bola(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.move_vel = 0.1     
        
    def mov(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)
        
    def kickou(self):
        self.ymove *= -1
        self.move_vel *= 0.9
        
    def bateu(self):
        self.xmove *= -1
        self.move_vel *= 0.9
    
    def reset(self):
        self.goto(0,0)
        self.xmove *= -1
        self.move_vel = 0.1