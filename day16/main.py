from turtle import Turtle, Screen

import another_module as mod

# print(mod.var)

t = Turtle() #object created with name t  with class Turtle from turtle module
#paranthesis to initialize or construct the object and save it in variable called t

#you can also import Turtle class as from turtle import Turtle

screen = Screen() #object created with name screen with class Screen from turtle module

print(screen.canvheight)

#to access the methods

screen.exitonclick()
