COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random as r


class CarManager():
    
    def __init__(self):
        self.allcars = []
        
        
    def create_car(self):
        random_chance = r.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(r.choice(COLORS))
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            random_y = r.randint(-250,250)
            new_car.goto(300, random_y)
            self.allcars.append(new_car)
    
    def move_cars(self):
        for car in self.allcars:
            car.backward(STARTING_MOVE_DISTANCE)
        
