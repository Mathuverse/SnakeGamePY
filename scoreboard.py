from turtle import Turtle

class Scoreboard(Turtle):
    #initialize the scoreboard at the start
    def __init__(self):
        super().__init__()
        self.score=0
        self.highscore=0
        self.color("white")
        self.penup()
        self.goto(0,350)
        self.write(f"Score: {self.score}", align='center',font=('Courier',30,'italic'))
        self.hideturtle()
    
    #adding points and reupdate scoreboard
    def add_Score(self):
        self.score += 1
        if self.score > self.highscore:
            self.highscore+=1
            print(self.highscore)
        self.clear()
        self.write(f"Score : {self.score}",align='center', font=('Courier', 30, 'italic'))

    #When gameover update Scoreboard
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAMEOVER, Highscore: {self.highscore}", align = 'center', font=('Courier', 50, 'italic'))
        
