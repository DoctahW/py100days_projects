from turtle import Turtle


class Placar(Turtle):
    
    def __init__(self):
        super().__init__()
        self.pontos = 0
        with open("jogo_da_cobrinha/data.txt") as data:
            self.maxim = int(data.read())
        self.penup()
        self.color("white")
        self.goto(0,240)
        self.speed("fastest")
        self.hideturtle()
        self.update_score()
        
        
    def update_score(self):
        self.clear()
        self.write(f"Sua pontuação é de {self.pontos} Maior: {self.maxim}",False, "center", ("Roboto",14,"normal"))
        
    
    def resetar(self):
        if self.pontos > self.maxim:
            self.maxim = self.pontos
            with open("jogo_da_cobrinha/data.txt", mode="w") as data:
                data.write(f"{self.maxim}")
        self.pontos = 0
        self.update_score()
    
    # def game_over_scrr(self):
    #     self.goto(0,0)
    #     self.write(f"FIM DE JOGO",False, "center", ("Roboto",14,"normal"))
    
    def acerto(self):
        self.pontos += 1
        self.update_score()
        
        