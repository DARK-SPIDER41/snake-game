from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 24, "normal")


class Score_Board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"score: {self.score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)
