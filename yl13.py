import turtle
from turtle import numinput

# Küsi kasutajalt joonlaua pikkus sentimeetrites
pikkus = numinput("Joonlaud", "Sisesta joonlaua pikkus sentimeetrites:", minval=1, maxval=100)

# Algseadistus
turtle.speed(0)
turtle.penup()
turtle.goto(-pikkus * 5 / 2, 0)  # Keskenda joonlaud ekraanile
turtle.pendown()

# Joonlaua joonistamine
for i in range(int(pikkus) + 1):
    if i % 5 == 0:
        # Pikem kriips iga 5 cm järel
        turtle.setheading(90)
        turtle.forward(20)
        turtle.backward(20)
        turtle.setheading(0)
        turtle.forward(5)

        # Number
        turtle.penup()
        turtle.setheading(90)
        turtle.forward(25)
        turtle.write(str(i), align="center", font=("Arial", 10, "normal"))
        turtle.backward(25)
        turtle.pendown()
    else:
        # Lühem kriips
        turtle.setheading(90)
        turtle.forward(10)
        turtle.backward(10)
        turtle.setheading(0)
        turtle.forward(5)

turtle.hideturtle()
turtle.done()
