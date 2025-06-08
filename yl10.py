import random




#Arvude keskmine 1

#Koostage Pythoni programm, mis küsib kasutajalt arve ükshaaval. Programm peaks jätkama arvude küsimist ja nende vastuvõtmist seni, kuni kasutaja jätab sisestuse tühjaks (st vajutab sisestusklahvi ilma midagi kirjutamata).
#Programm peab kasutama while-tsüklit arvude küsimiseks ja nende salvestamiseks.
#Pärast seda, kui kasutaja lõpetab arvude sisestamise peab programm arvutama ja väljastama kõikide sisestatud arvude keskmise väärtuse.


arvud = []

while True:
    sisend = input("Sisesta arv (või vajuta Enter lõpetamiseks): ")
    if sisend == "":
        break
    try:
        arv = float(sisend)
        arvud.append(arv)
    except ValueError:
        print("Palun sisesta sobiv arv!")

if arvud:
    keskmine = sum(arvud) / len(arvud)
    print(f"\nSisestasid {len(arvud)} arvu.")
    print(f"Arvude keskmine on: {keskmine:.2f}")
else:
    print("Sa ei sisestanud ühtegi arvu.")
    





#Arvu äraarvamise mäng 2

#Kirjutage Pythoni skript, mis simuleerib arvu äraarvamise mängu.
#Programm peab esmalt genereerima juhusliku arvu vahemikus 1 -10.
#Seejärel küsib programm kasutajalt arve, püüdes ära arvata genereeritud arvu. Kasutaja jätkab arvude sisestamist, kuni ta arvab õige arvu ära. Iga kord, kui kasutaja sisestab arvu, peab programm andma tagasisidet, kas pakutud arv on õige või mitte.
#Pärast õige arvu äraarvamist teavitab programm kasutajat, mitmenda katsega õige arv ära arvati, ja küsib, kas kasutaja soovib mängida uuesti.
#Kui kasutaja vastab jaatavalt, genereerib programm uue juhusliku arvu ja mäng algab otsast peale.
#Kui kasutaja otsustab mitte jätkata, tänab programm kasutajat mängus osalemise eest ja kuvab kõik senised tulemused: mitmenda katsega igal korral õige arv ära arvati.
#Programm peab kasutama while-tsüklit nii arvude sisestamise protsessi juhtimiseks kui ka mängu kordamise otsustamiseks.
import random

tulemused = []
loop = True

while loop:
    katsed = 0
    arv = random.randint(1, 10)
    print(arv)  # Testimiseks võid selle hiljem eemaldada

    while True:
        katsed += 1
        try:
            vastus = int(input("Arva ära arv 1-10: "))
        except ValueError:
            print("Palun sisesta arv!")
            continue

        if vastus == arv:
            print("Õige!")
            print(f"Arvasid {katsed} korda.")
            tulemused.append(katsed)
            uuesti = input("Kas soovid veel? (j/e): ")
            if uuesti.lower() == "j":
                break  # alustab uut mängu
            else:
                loop = False  # lõpetab mängu
                break
        else:
            print("Proovi uuesti!")

print("Mäng läbi.")
print("Tulemused:", tulemused)




