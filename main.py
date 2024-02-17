import time 
from turtle import Screen,Turtle
from food import Food
from scoreboard import Scoreboard
from snake import Snake

#initialize all componenents
screen = Screen()
snake = Snake()
food = Food()
score = Scoreboard()
speed = 0.05
game_is_on = True

#Screen setup
screen.setup(800,800)
screen.bgcolor("black")
screen.tracer(0)

#Screen listener for keyboard bind
screen.listen()
screen.onkey(key="w",fun=snake.up)
screen.onkey(key="s",fun=snake.down)
screen.onkey(key="d",fun=snake.right)
screen.onkey(key="a",fun=snake.left)

#Game loop
while game_is_on:
    time.sleep(speed)
    screen.update()
    snake.moving()

    #Detect food collision
    if food.distance(snake.head) < 15:
        food.random_location()
        score.add_Score()
        snake.moving()

    #Detect wall
    if snake.head.xcor() > 380 or snake.head.xcor()< -380 or snake.head.ycor() > 380 or snake.head.ycor()< -385:
        score.game_over()
        game_is_on = False
    
    #Detection Collision with own tail
    for part in snake.segments:
        if part == snake.head:
            pass
        elif snake.head.distance(part) < 10:
            score.game_over()
            game_is_on = False

screen.exitonclick()