import turtle               #imports turtle

j = turtle.Turtle()         #initaites turtle with name j
wn = turtle.Screen()        #initates screen with name wn


def circle(dist):           #function repeats forwardleft 360 times
    for i in range(360):    #takes in argument dist which sets the size
        j.forward(dist)
        j.left(1)
        
def move(dis, ang):         #function takes in a distance and direction to move the pen
    j.penup()
    j.left(ang)
    j.forward(dis)
    j.pendown()

def square(dis):            #draws square takes in size as dist
    for i in range(4):
        j.forward(dis)
        j.left(90)

def triange(dis):           #draws triangle takes in size as dist
    for i in range(3):
        j.forward(dis)
        j.left(120)


circle(2)       #calls circle of size 2
move(100,180)   #moves back 100 steps
square(150)     #call square size 150   
move(250, 180)  #move 250 backwards
triange(150)    #draw triangle size 150
