from turtle import Turtle

PADDLE_MOVE = 40
class Paddle(Turtle):

	def __init__(self, position):
		super().__init__()
		self.color("white")
		self.shape("square")
		self.turtlesize(stretch_wid=5, stretch_len=1)
		self.penup()
		self.goto(position)


	def go_up(self):
		new_y = self.ycor() + PADDLE_MOVE
		self.goto(x=self.xcor(), y=new_y)

	def go_down(self):
		new_y = self.ycor() - PADDLE_MOVE
		self.goto(x=self.xcor(), y=new_y)

