from turtle import Turtle

class Placar(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore = 0
        self.rscore = 0
        self.update_placar()

    def update_placar(self):
        self.clear() 
        self.goto(-100, 200)
        self.write(self.lscore, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.rscore, align="center", font=("Courier", 80, "normal"))
        
    def r_point(self):
        self.rscore += 1
        self.update_placar()
    
    def l_point(self):
        self.lscore += 1
        self.update_placar()