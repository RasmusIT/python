#Rasmus Ojala 15.11.2024
# H11
import turtle

#def tervita (a,b):
#    print("tere "+a)

# Kirjuta funktsioon pikim_sona(), mis võtab sisendiks sõnade listi ja tagastab pikima sõna pikkuse. Prindi tulemus konsooliaknasse.





def pikim_sona():
pikimSona = 0
for sona in a:
    if a.len(sona)>pikimSona:
        pikimSona = len(sona)
    print(pikimSona)

sonad = ["üks", "kaks", "kolm", "kuusteist"]


pikim_sona(sonad)


# Kirjuta funktsioon nimega kolm_pikimat_sona(), mis analüüsib sõnade listi ja leiab kolm kõige pikemat sõna. Lisa kontroll juhuks, kui sõnade arv pole piisav.

def kolm_pikimat_sona():
    uusSonastik = {}
    uusSonastik['üks'] = 3
    for sona in a:
        uusSonastik[sona] = len(sona)
    jar = sorted(uusSonastik.items(), key=lambda x:x[1], reverse=True)
    if len(a)<3:
        print("Sõnade arv pole piisav")
    else:
        for i in range(3):
            print(jar[i][0])

kolm_pikimat_sona(sonad)


#Kirjuta funktsioon, mis kontrollib, kas kahest sõnast koosnev sõne algab sama tähega.
#print(sarnased_esitahed('Vapper Vares')) # peaks tagastama True
#print(sarnased_esitahed('Lahe Känguru')) # peaks tagastama False

def sarnased_esitahed(a):
    tykk = a.split(" ")
    if (tykk[0][0]).lower()==(tykk[1][0]).lower():
        return "True"
    else:
        return "False"

print(sarnased_esitahed('Vapper Vares'))
print(sarnased_esitahed('Lahe känguru'))



# Kilpkonn – kirjutada programm, mis lubab kasutajal valida kujundite tüübi (viisnurk, ring, ruut või suvaline) ja arvu. Programm joonistab seejärel antud arvu kujundeid valitud tüübiga või juhul, kui valik on “suvaline”, valib programm ise juhuslikult kujundi tüübi iga kujundi jaoks.
# Millist kujundit soovid joonistada (viisnurk, ring, ruut, suvaline)? Suvaline
# Mitu kujundit soovid joonistada? 5

# [Joonistab 5 kujundit, igaüks juhuslikult valitud tüübiga suvalistesse kohtadesse]
# Pärast joonistamist peaks programm pakkuma võimalust sisestada uued väärtused või väljuda programmist, jättes sisendi tühjaks.

print("-------------- Joonistame kujundeid --------------")
print("Vali kujund: \n1 viisnurk \n2 ring \n3 ruut \n4 suvaline")
kujund = int(input("Sisesta number"))
arv = int(input("Mitu kujundit tahad (1-100): "))

def viisnurk(k):
    print("Joonistan viisnurga")
def ring(k):
    print("Joonistan ringi")
def ruut(k):
    print("Joonistan ruudu")
    for j in range(a):
    turtle.speed(0)
    turtle.penup()
    turtle.goto(random.randint(-400,400),random.randint(-400,-400))
    turtle.pendown()
    turtle.rt(random.randint(0,90))
    for i in range(4):
        turtle.fd(100)
        turtle.lt(90)

def suvaline():
  for i in range(k):
    my_list = [viisnurk, ring, ruut]
    random.choice(my_list)(1)

print("-----------Minu fancy programm-------------")

loop = 1

