from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0),(-60,0), (-80,0)]

class Snake:

    #initialize snake at the start
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    #create the snake and position
    def create_snake(self):
        for position in STARTING_POSITION:
            new_snake_body = Turtle("square")
            new_snake_body.color("white")
            new_snake_body.penup()
            new_snake_body.goto(position)
            self.segments.append(new_snake_body)

    #adding extra length to the snake body
    def add_segment(self):
        new_part = Turtle("square")
        new_part.color("black")
        new_part.penup()
        self.segments.append(new_part)
    
    #moving mecanism non stop for the snake 
    def moving(self):
        for position in range(len(self.segments)-1,0,-1):
            new_x = self.segments[position-1].xcor()
            new_y = self.segments[position-1].ycor()
            self.segments[position].goto(new_x,new_y)
            self.segments[position].color("white")
        self.head.fd(10)

    #Different motion up down left right
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
