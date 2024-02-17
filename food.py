import random
from turtle import Turtle

class Food(Turtle):

    #initializing Food class
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.shapesize(0.5,0.5)
        self.random_location()

    #spawn the food in random location
    def random_location(self):
        self.goto(random.randint(-350,350),random.randint(-350,350))