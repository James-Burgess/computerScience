import turtle

j = turtle.Turtle()
wn = turtle.Screen()
x = 2

def circle(x):
    for i in range(360):
        j.forward(x)
        j.left(1)

def move(dis, ang):
    j.penup()
    j.left(ang)
    j.forward(dis)
    j.pendown()

def square(dis):
    for i in range(4):
        j.forward(dis)
        j.left(90)

def triange(dis):
    for i in range(3):
        j.forward(dis)
        j.left(120)

circle(x)
move(100,180)
square(150)
move(250, 180)
triange(150)
