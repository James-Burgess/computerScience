import turtle 

polygon = turtle.Turtle()

num_sides = int(input("how many sides: "))
side_length = 70
angle = 360.0 / num_sides

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
    
turtle.done()