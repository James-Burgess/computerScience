import turtle
from random import randint
wn = turtle.Screen()
wn.colormode(255)
boo = turtle.Turtle()
boo.speed(0)
wn.bgcolor("black")
boo.shape("turtle")

def circle():
	for i in range(180):
		boo.fd(5)
		boo.rt(2)
for j in range(36):
	r = randint(0, 255)
	g = randint(0, 255)
	b = randint(0, 255)

	boo.pencolor((r, g, b))
	boo.rt(10)
	circle()
	
wn.mainloop()