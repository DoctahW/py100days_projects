from turtle import Turtle

# É uma boa prática definir a fonte como uma constante
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.lscore = 1
        # Adicione a linha abaixo para posicionar o placar
        self.goto(-280, 250) 
        self.update_placar()  # <- ESSA É A LINHA QUE FALTAVA

    def update_placar(self):
        self.clear()
        self.write(f"Level: {self.lscore}", align="left", font=FONT)

    def l_point(self):
        self.lscore += 1
        self.update_placar()
    
    def game_over_scrr(self):
        self.goto(0,0)
        self.write(f"FIM DE JOGO", align="center", font=(FONT))