import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

bicho = Player()
controle = CarManager()
placar = Scoreboard()

screen.listen()
screen.onkey(bicho.move,"w")

game_is_on = True
while game_is_on:
    time.sleep(bicho.move_vel)
    screen.update()
    
    controle.create_car()
    controle.move_cars()
    
    for car in controle.allcars:
        if bicho.distance(car) < 30:
            game_is_on = False
            placar.game_over_scrr()
            
    if bicho.ycor() > 280:
        bicho.reseti()
        placar.l_point()
        

screen.exitonclick()
