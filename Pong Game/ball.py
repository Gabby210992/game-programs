from turtle import Turtle

class Ball(Turtle):

	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.color("white")
		self.setheading(35)
		self.penup()
		self.x_cor = 10
		self.y_cor = 10
		self.move_speed = 0.1


	def move(self):
		new_x = self.xcor() + self.x_cor
		new_y = self.ycor()	+ self.y_cor
		self.goto(x=new_x, y=new_y)

	def y_bounce(self):
		self.y_cor *= -1

	def x_bounce(self):
		self.x_cor *= -1
		self.move_speed *= 0.9
	def reset_position(self):
		self.move_speed = 0.1
		self.goto(0, 0)
		self.x_bounce()