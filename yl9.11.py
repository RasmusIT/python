import turtle
screen = turtle.Turtle()
t.speed(0)
t.hideturtle()

num_points = 12
raidus = 150
angle = 360 / num_points

points = []
for i in range(num_points):
    t.penup()
    t.goto(0,0)
    t.setheading( i * angle)
    