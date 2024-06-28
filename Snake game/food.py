from turtle import Turtle
import random

COR_1 = -280
COR_2 = 280


class Food(Turtle):

	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.penup()
		self.shapesize(stretch_len=0.5, stretch_wid=0.5)
		self.color("yellow")
		self.speed("fastest")
		random_x = random.randint(a=COR_1, b=COR_2)
		random_y = random.randint(a=COR_1, b=COR_2)
		self.refresh()

	def refresh(self):
		random_x = random.randint(a=COR_1, b=COR_2)
		random_y = random.randint(a=COR_1, b=COR_2)
		self.goto(random_x, random_y)

