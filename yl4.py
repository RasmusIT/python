#  16.10.2024 Rasmus
# Ülesanded 4

import turtle


# 4) Ringi pindala ja Turtle
try:
    r = int(input("Sisesta ringi raadius: "))
    r = 10
    s = 3.14*r ** 2
    p = 2 * 3.14 * r
    print(f"Ringi pindala on {s:.2f} ka ümbermõõt on {p:.2f}")
    turtle.circle(r*2, 360)
    turtle.done()
except:
    print("Sisestus vale!")


# 5) Kingituste pakkimine
try:
    kast = 5
    kingitusteArv = 23
    komplektid = kingitusteArv//kast #täisarvu saamine
    yle = kingitsuteArv%kast #jäägi saamine
    print(f"Saad teha {komplektid} täis kinkekasti. üle jääb {ylr} kingitust. ")
except:
    print("Lisasid koguse valesti")


# 3) Faili allalaadimine
try:
    failiSuurus = 500
    downlKiirus = 20
    aeg = failiSuurus/downlKiirus
    print(f"Allalaadimiseks kulub {aeg} sekundit")
except:
    print("Sa ei sisestanud täisarvu!")


# 2) Raamatute allahindlus
ale = 0.3
arv = 12.3
kogus = int(input("Lisa raamatute kogus: "))
summa = (hind-(hind * ale)) * kogus
print(f"{kogus} raamatu hind soodustusega on {summa:.2f}€. ")

# 1) Aia pikkus
a = int(input("Lisa 1 külg: "))
b = int(input("Lisa 2 külg: "))
p = 2* (a+b)
print (f"Aia kogupikkus on{p} meetrit. ")