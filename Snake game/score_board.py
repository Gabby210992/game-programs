from turtle import Turtle


with open("data.txt") as score_data:
	high_score = score_data.read()


ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")


class ScoreBoard(Turtle):

	def __init__(self):
		super().__init__()
		self.score = 0
		self.high_score = int(high_score)
		self.penup()
		self.color("white")
		self.goto(x=0, y=280)
		self.update_score()
		self.hideturtle()

	def update_score(self):
		self.clear()
		self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

	def increase_score(self):
		self.score += 1
		self.update_score()

	def reset(self):
		if self.score > self.high_score:
			self.high_score = self.score
			with open("data.txt", "w") as score_data:
				score_data.write(f"{self.high_score}")
		self.score = 0
		self.update_score()
