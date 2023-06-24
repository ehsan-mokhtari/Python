import turtle

t = turtle.Turtle()
t.screen.bgcolor("white")
t.left(90)
t.speed(50)
t.color('purple')
t.pensize(4)

#x is the number of iteration
def draw(x):
    if x<10:
        return
    else:
        t.forward(x)
        t.left(25)
        draw(3*x/4)
        t.right(50)
        draw(3*x/4)
        t.left(25)
        t.backward(x)

draw(90)
t = turtle.done()