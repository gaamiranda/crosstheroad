import turtle

class Scoreboard(turtle.Turtle):
	def __init__(self):
		super().__init__()
		self.score = 0
		self.penup()
		self.hideturtle()
		self.color("black")
		self.goto(-20, 265)
		self.updatescoreboard()

	def updatescoreboard(self):
		self.clear()
		self.write(f"Level: {self.score}", align="center", font=("Arial", 20, "normal"))
		self.score += 1
		
	def finish(self):
		self.goto(0,0)
		self.write("GAME OVER", align="center", font=("Arial", 50, "normal"))