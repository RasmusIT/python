# 18.10.2024 Rasmus
# ülesanne 5
import random
import turtle


# 1. Ilmaennustuse rakendus
try:
c = input("Lisa kraadid: ")
if c < 0:
    print("Kanna talveriideid")
elif c>=0 and c<15:
    print("Kanna kevad-sügis rõivaid")
else:
    print("Kanna suveriideid")
except:
    print("Pane täisarv!")


# 2. Matemaatika test
a = random.ramdint(1,10)
b = random.ramdint(1,10)
vastus = int(input(str(a)+"*"+str(b)+"="))
if a*b == vastus:
    print("Tubli!")
else:
    print("Vale!")


# 3. Vanusepiiranguga üritus
vanus = int(input("Lisa vanus"))
if vanus >= 18:
    print("Saab sisse!")
else:
    print("Liiga noor!")


# 4. Mündiviskamise äraarvamine koos juhuslikkusega
# kull = 1
# kiri = 0
mynt = random.randint(0,1)
arva = int(input("Vali kull või kiri: "))
if (mynt == 0: and arva == "kiri") or (mynt == 1 and arva == "kull"):
    vastus = "green"
else:
    vastus = "red"
print(mynt)
turtle:color(vastus)
turtle.circle(100)
turtle.done()