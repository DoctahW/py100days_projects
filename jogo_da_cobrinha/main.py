import turtle as t
from cobrinha import Snake
from food import Comida
from placar import Placar
import time


screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Jogo da cobrinha")

cobra = Snake()
alimento = Comida()
placar = Placar()

screen.listen()
screen.onkey(cobra.up,"Up")
screen.onkey(cobra.down,"Down")
screen.onkey(cobra.left,"Left")
screen.onkey(cobra.right,"Right")


game_is_on = True
while game_is_on == True:
    screen.update()
    time.sleep(0.1)
    cobra.move_cobra()
    
    if cobra.head.distance(alimento) < 15:
        alimento.refresh()
        placar.acerto()
        cobra.maior()
    
    if abs(cobra.head.xcor()) > 280 or abs(cobra.head.ycor()) > 280:
        placar.resetar()
        cobra.reset()
    
    
    for segment in cobra.segments[1:]:
        if cobra.head.distance(segment) < 10:
            placar.resetar()
            cobra.reset()

    
    
        





screen.exitonclick()



