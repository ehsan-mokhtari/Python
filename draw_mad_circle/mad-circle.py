import turtle

trtl = turtle.Turtle()
scrn = turtle.Screen()

scrn.bgcolor('white')
trtl.pencolor('black')
trtl.speed(0)
trtl.penup()
trtl.goto(0,100)
trtl.pendown()
a,b=0,0
while True:
    trtl.forward(a)
    trtl.right(b)
    a,b=a+4,b+2
    if b==200:
        break
    trtl.hideturtle()
turtle.done()    