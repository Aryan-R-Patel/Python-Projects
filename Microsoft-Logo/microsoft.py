# importing the turtle library
import turtle

# main code
t = turtle.Turtle()
t.speed(5)
t.hideturtle()

colors = ["blue", "orange", "green", "red"]
position = [(-175,-175), (5,-175), (5,5), (-175,5)]

for (x,y),color in zip(position, colors):
    t.penup()
    t.setposition(x,y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for i in range(4):
        t.forward(170)
        t.left(90)
    t.end_fill()

turtle.done()