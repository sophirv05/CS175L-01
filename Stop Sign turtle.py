#Sophia Ramirez Velandia
#Exercise 4-19 Stop Sign
#CS 175L
#Prof Gil

import math
import turtle

#Named constants
window_width = 400
window_height = 400
num_sides = 8
length = 100
angle = 45

# Size the window.
turtle.setup(window_width, window_height)

# Initialize the turtle.
turtle.penup()
turtle.goto(-50,100)
turtle.pendown()
turtle.shape('turtle')

turtle.pensize(5)
turtle.color('black')
turtle.fillcolor('red')
turtle.begin_fill()

for stop in range(num_sides):
    turtle.pendown()
    turtle.forward(length)
    turtle.right(angle)
turtle.end_fill()

turtle.penup()
turtle.goto(-75,-70)
turtle.color("white")
turtle.write("STOP", font=("Impact",80))
turtle.hideturtle()





