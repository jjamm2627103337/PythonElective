import turtle

t = turtle.Turtle()

t.screen.bgcolor("black")
t.color("red")
t.begin_fill()
t.fillcolor("pink")
for i in range(4):
    t.forward(100)
    t.right(90)

t.end_fill()

turtle.done()