import turtle
myPen = turtle.Turtle()
myPen.shape("arrow")
wn = turtle.Screen()

myPen.color("red")
myPen.speed(5) #Set the speed of the turtle



for i in range(0,11):


    yFrom=10-i
    xTo=i


    myPen.penup()
    myPen.goto(0,20*yFrom)
    myPen.pendown()
    myPen.goto(20*xTo,0)





wn.mainloop()