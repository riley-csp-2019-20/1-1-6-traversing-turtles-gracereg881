#   a116_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic","circle","arrow"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold","magenta","brown"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  new_color = turtle_colors.pop()
  t.pencolor(new_color)
  t.fillcolor(new_color)
  my_turtles.append(t)


# the starting point
startx=0
starty=0

count=1

# the shapes start moving
for t in my_turtles:
	t.penup()
	t.goto(startx, starty)
	t.pendown()
	t.right(45*count)
	t.forward(100)
	direction=t.heading()
	count+=1

	
  


# makes the shapes apart from each other
	startx = t.xcor()
	starty = t.ycor()

wn = trtl.Screen()
wn.mainloop()