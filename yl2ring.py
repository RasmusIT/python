import turtle

# Setup screen
screen = turtle.Screen()
screen.title("Olümpiarõngad ja Sinu Nimi")
screen.setup(width=500, height=400)

# Define ring positions and colors
positions = [(-120, 50), (0, 50), (120, 50), (-60, 0), (60, 0)]
colors = ["blue", "black", "red", "yellow", "green"]

# Draw rings
turtle.speed(0)
turtle.pensize(6)
for pos, color in zip(positions, colors):
    turtle.penup()
    turtle.goto(pos)
    turtle.pendown()
    turtle.color(color)
    turtle.circle(50)


turtle.done()