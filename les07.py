# codding utf-8
import turtle
#import tkSimpleDialog # 2.x python
import random

turtle.circle(20)

answer = ''

while answer != 'n':
    answer = turtle.textinput("Нарисовать окружность", "y/n")
    # answer = tkSimpleDialog.askstring("Нарисовать окружность", "Y/N") # 2.x python

    if answer == 'y':
        # turtle.circle(30)
        turtle.penup()
        turtle.goto(random.randrange(-300, 300), random.randrange(-300, 300))
        turtle.pendown()
        turtle.fillcolor(random.random(), random.random(), random.random())
        turtle.begin_fill()
        turtle.circle(random.randrange(1, 100))
        turtle.end_fill()
    else:
        pass
