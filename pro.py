import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon=turtle.Turtle()
num_side=4
sidel=60
angle=360.0/num_side
for i in range(num_side):
    polygon.forward(sidel)
    polygon.right(angle)
    polygon.forward(sidel)
    polygon.right(angle)
    polygon.forward(sidel)
    polygon.right(angle)
    polygon.forward(sidel)
    polygon.right(angle)
turtle.done     