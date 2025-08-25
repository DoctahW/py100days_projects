import turtle as t
from paddle import Paddle
from ball import Bola
from scoreboard import Placar
import time

screen = t.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG NO PYTHON")
screen.tracer(0)

paddle_hero = Paddle((-350,0))
evil_paddle = Paddle((350,0))
bola = Bola()
placar = Placar()

screen.listen()
screen.onkey(paddle_hero.move_up,"Up")
screen.onkey(paddle_hero.move_down,"Down")
screen.onkey(evil_paddle.move_up,"w")
screen.onkey(evil_paddle.move_down,"s")



game_is_on = True
while game_is_on is True:
    time.sleep(bola.move_vel)
    screen.update()
    bola.mov()
    
    if abs(bola.ycor()) > 280:
        bola.kickou()
    
    if bola.distance(paddle_hero) < 50 and bola.xcor() < -320 or bola.distance(evil_paddle) < 50 and bola.xcor() > 320:
        bola.bateu()
        
        
    if abs(bola.xcor()) > 380:
        bola.reset()
        placar.l_point()
        
    
    if abs(bola.ycor()) < -380:
        bola.reset()
        placar.r_point()
        
        
screen.exitonclick()