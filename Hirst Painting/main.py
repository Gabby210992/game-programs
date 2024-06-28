import turtle as t
import random

tim = t.colormode(255)
tim = t.Turtle()
t_screen = t.Screen()
tim.hideturtle()
tim.speed("fastest")
color_list = [(56, 8, 25), (250, 246, 237), (32, 33, 128), (22, 17, 67), (34, 16, 8), (155, 77, 41), (207, 157, 99),
			  (229, 232, 241), (232, 210, 115), (116, 26, 59), (51, 77, 165), (230, 80, 51), (156, 22, 11),
			  (249, 240, 245), (245, 250, 247), (118, 63, 82), (183, 149, 55), (97, 70, 15), (158, 162, 189),
			  (15, 25, 21)]
y = -160
tim.penup()
tim.setpos(-200, -200)
for row in range(10):
	for _ in range(10):
		tim.dot(20, random.choice(color_list))
		tim.forward(40)

	tim.setpos(-200, -200)
	tim.sety(y)
	y += 40

t_screen.exitonclick()