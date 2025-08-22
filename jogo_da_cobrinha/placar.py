from turtle import Turtle

class Placar(Turtle):
    
    def __init__(self):
        super().__init__()
        self.pontos = 0
        self.penup()
        self.color("white")
        self.goto(0,240)
        self.speed("fastest")
        self.hideturtle()
        self.write(f"Sua pontuação é de {self.pontos}",False, "center", ("Roboto",14,"normal"))
    
    def game_over_scrr(self):
        self.goto(0,0)
        self.write(f"FIM DE JOGO",False, "center", ("Roboto",14,"normal"))
    
    def acerto(self):
        self.pontos += 1
        self.clear()
        self.write(f"Sua pontuação é de {self.pontos}",False, "center",("Roboto",14,"normal"))
        
        