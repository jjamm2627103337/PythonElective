import turtle

t = turtle.Turtle()

#t.circle(100)

""" for i in range(3):
    t.forward(100)
    t.left(120) """

""" for i in range(2):
    t.forward(100)
    t.left(120)
    t.forward(50)
    t.left(60) """

""" for i in range(5):
    t.forward(100)
    t.left(144) """
t.begin_fill()
t.fillcolor("red")    
for i in range(6):
    t.forward(100)
    t.right(60)
t.end_fill()

turtle.done()