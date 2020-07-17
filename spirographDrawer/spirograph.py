import turtle

turtle.bgcolor('white')
turtle.pensize(2)
turtle.speed(0)

for i in range(7):
    for j in ['red', 'blue', 'green' , 'yellow', 'magenta']:
        turtle.color(j)
        turtle.circle(100)
        turtle.left(10)