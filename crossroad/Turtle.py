import turtle

class Turtle(turtle.Turtle):
	def __init__(self):
		super().__init__()
		self.penup()
		self.color("green")
		self.shapesize(1.2, 1.2)
		self.shape("turtle")
		self.setheading(90)
		self.goto(0, -260)
	
	def moveup(self):
		newy = self.ycor() + 30
		self.goto(self.xcor(), newy)