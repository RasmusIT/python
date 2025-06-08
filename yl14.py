import turtle

# Seaded
turtle.title("Hiirega joonistamine ja klaviatuuriga värvi muutmine")
turtle.speed(0)
turtle.hideturtle()
turtle.colormode(255)

# Globaalne värvimuutuja
vaartus_varv = "black"

# Kujundite salvestamiseks
joonistatud_kujundid = []

# Kujundi joonistamise funktsioon (ruut)
def joonista_kuju(x, y):
    kujund = turtle.Turtle()
    kujund.penup()
    kujund.goto(x, y)
    kujund.pendown()
    kujund.color(vaartus_varv)
    kujund.begin_fill()
    for _ in range(4):
        kujund.forward(40)
        kujund.right(90)
    kujund.end_fill()
    kujund.hideturtle()
    joonistatud_kujundid.append(kujund)

# Kustutamisfunktsioon (hiire parem klikk)
def kustuta_kujundid(x, y):
    for kujund in joonistatud_kujundid:
        kujund.clear()
        kujund.hideturtle()
    joonistatud_kujundid.clear()

# Värvi muutmise funktsioonid
def muuda_punaseks():
    global vaartus_varv
    vaartus_varv = "red"

def muuda_roheliseks():
    global vaartus_varv
    vaartus_varv = "green"

def muuda_siniseks():
    global vaartus_varv
    vaartus_varv = "blue"

# Sidumised
turtle.onscreenclick(joonista_kuju, 1)  # Vasak klikk
turtle.onscreenclick(kustuta_kujundid, 3)  # Parem klikk

turtle.listen()
turtle.onkey(muuda_punaseks, "r")
turtle.onkey(muuda_roheliseks, "g")
turtle.onkey(muuda_siniseks, "b")

# Käivitamine
turtle.done()
