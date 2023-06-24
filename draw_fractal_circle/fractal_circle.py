import turtle

turtl = turtle.Turtle()

turtl.screen.bgcolor('black')
turtl.pencolor('purple')
turtl.speed(0)
temp=0
dist=0
while True:
    for i in range (4):
        turtl.forward(80)
        turtl.right(90)
    turtl.right(15)
    temp = temp+ 1
    if temp >= 26:
        turtl.forward(50)
        temp=0
        dist = dist+1
        if dist >=12:
            break

turtl.hideturtle()
turtle.done()