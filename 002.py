import turtle

t = turtle.Turtle()

t.screen.bgcolor("black")
t.width(2)
t.color("red")
t.begin_fill()
t.fillcolor("white")
for j in range(4):
    for i in range(10):
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
    t.right(90)
t.end_fill()

t.right(90)
t.forward(30)

turtle.done()