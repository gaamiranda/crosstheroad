import turtle
from Turtle import Turtle
import time
from scoreboard import Scoreboard
from cars import Car

def closewindow():
	screen.bye()


screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Turtle()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(closewindow, "q")
screen.onkey(turtle.moveup, "Up")

cars = []
game_is_on = 1
i = 0
sleep = 0.2
while game_is_on:
	if i % 6 == 0:
		car = Car()
		cars.append(car)
	i += 1
	screen.update()
	time.sleep(sleep)
	if turtle.ycor() > 80:
		turtle.goto(0, -260)
		scoreboard.updatescoreboard()
		sleep *= 0.9
	for char in cars:
		if abs(turtle.xcor() - char.xcor()) < 30:
			if abs(turtle.ycor() - char.ycor()) < 10:
				game_is_on = 0
				break
		char.moveleft()
scoreboard.finish()


















screen.exitonclick()