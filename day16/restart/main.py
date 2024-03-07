from another_module import value
from turtle import Turtle, Screen
# print(value)

tr = Turtle()
print(tr)
tr.shape("turtle")
tr.color("red","green")
tr.pendown()
tr.forward(100)
tr.left(90)
tr.forward(100)
tr.right(90)
tr.forward(100)
tr.right(180)
tr.forward(100)
tr.right(180)
tr.forward(100)
tr.right(400)

my_screen = Screen() #creating an object from screen class.. the name of object is my_Screen
print(my_screen.canvheight) #print canvas height of screen
my_screen.exitonclick() #myscreen object having an attribute exit on click.
