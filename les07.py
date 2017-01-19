# codding utf-8
import turtle
#import tkSimpleDialog # 2.x python
import random
import math


def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def draw_circle(rad, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(rad)
    turtle.end_fill()

turtle.speed(0)

# baraban
gotoxy(0, 0)
turtle.circle(80)
gotoxy(0, 160)
draw_circle(5, 'red')

# bullets
phi = 360 / 7
r = 50

for i in range(0, 7):
    phi_rad = phi * i * math.pi / 180.0
    gotoxy(math.sin(phi_rad)*r, math.cos(phi_rad) * r + 57)
    turtle.circle(22)


gotoxy(math.sin(phi_rad)*r, math.cos(phi_rad) * r + 57)
draw_circle(22, 'brown')

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
