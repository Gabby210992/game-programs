import colorgram
from turtle import Turtle, Screen
colors = colorgram.extract("da7decdbcad344848a5be7cc3a04306e.jpg", 20)

color_list = []
for color in colors:
	r = color.rgb.r
	g = color.rgb.g
	b = color.rgb.b
	new_color = (r, g, b)
	color_list.append(new_color)

tim = Turtle()
screen = Screen()
print(color_list)