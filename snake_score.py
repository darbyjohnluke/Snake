from turtle import Turtle, Screen

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.write(f"Score: {self.score}", align= "center", font=("Courier", 15, "normal") )

    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score: {self.score}", align= "center", font=("Courier", 15, "normal") )

    def game_over(self):
        self.goto(0, 0)
        self.color("lime green")
        self.write("GAME OVER", align= "center", font=("Courier", 33, "normal") )



# arg mov allign font