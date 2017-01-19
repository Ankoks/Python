# codding utf-8
import turtle
#import tkSimpleDialog # 2.x python
import random
import math

import mr_robot

# bullets
PHI = 360 / 7
R = 50

turtle.speed(0)


def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def draw_circle(rad, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(rad)
    turtle.end_fill()


def draw_pistol(x, y):
    # base circle
    gotoxy(x, y)
    turtle.circle(80)
    # mushka
    gotoxy(x, y + 160)
    draw_circle(5, 'red')

    # baraban
    for i in range(0, 7):
        phi_rad = PHI * i * math.pi / 180.0
        gotoxy(x + math.sin(phi_rad) * R, y + math.cos(phi_rad) * R + 57)
        draw_circle(21, 'white')


def rotate_pistol(x, y, start):
    for i in range(start, random.randrange(7, 50)):
        phi_rad = PHI * i * math.pi / 180.0
        gotoxy(x + math.sin(phi_rad) * R, y + math.cos(phi_rad) * R + 57)
        draw_circle(21, 'brown')
        draw_circle(21, 'white')

    gotoxy(x + math.sin(phi_rad) * R, y + math.cos(phi_rad) * R + 57)
    draw_circle(21, 'brown')

    return i % 7


# baraban
draw_pistol(15, 200)

answer = ''
start = 0

while answer != 'n':
    answer = turtle.textinput("Want play?", "y/n")
    # answer = tkSimpleDialog.askstring("Нарисовать окружность", "Y/N") # 2.x python

    if answer == 'y':

        start = rotate_pistol(15, 200, start)

        if start == 0:
            gotoxy(-150, 200)
            turtle.write("You lost", font=("Arial", 18, "normal"))
            randomchoose = random.randrange(0, 2)
            if randomchoose == 0:
                mr_robot.double_files('test')
            else:
                mr_robot.random_delete('test')
    else:
        pass

