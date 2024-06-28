from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time


COR_1 = 290
COR_2 = -290

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("Black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(snake.down, key="Down")
screen.onkey(snake.left, key="Left")
screen.onkey(snake.right, key="Right")

game_is_on = True

while game_is_on:
	screen.update()
	time.sleep(0.1)

	snake.move()

	if snake.head.distance(food) < 15:
		score.increase_score()
		snake.extend()
		food.refresh()

	if snake.head.xcor() > COR_1 or snake.head.xcor() < COR_2 or snake.head.ycor() > COR_1 or snake.head.ycor() < COR_2:
		snake.reset()
		score.reset()

	for segment in snake.segments[1:]:
		if segment == snake.head:
			pass

		elif snake.head.distance(segment) < 10:
			score.reset()
			snake.reset()


screen.exitonclick()
