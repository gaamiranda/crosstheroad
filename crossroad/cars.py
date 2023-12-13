import turtle
import random

LOCATIONS = [(270, -230), (270, -200), (270, -170), (270, -140), (270, -110), (270, -80), (270, -50), (270, -20), (270, 10), (270, 40), (270, 70)]
COLORS = ["orange", "blue", "red", "black", "purple"]
class Car(turtle.Turtle):
	def __init__(self):
		super().__init__()
		self.shape("square")
		self.shapesize(1, 3)
		self.penup()
		self.color(random.choice(COLORS))
		self.goto(random.choice(LOCATIONS))
		self.setheading(180)

	def moveleft(self):
		self.forward(20)
		
