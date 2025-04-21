import turtle
turtle.Screen().bgcolor("turquoise")
turtle.Screen().setup(300,400)
polygon=turtle.Turtle()
num_side=int(input("ENTER THE NUMBER OF SIDES"))
sidel=float(input("ENTER THE LENGTH OF SIDES"))
angle=360.0/num_side
for i in range(num_side):
    polygon.forward(sidel)
    polygon.right(angle)    
turtle.done()    