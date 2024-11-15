# 24.10.2024 Rasmus
# Ülesanne 9

import random

# Genereeri ja kuva arvud arvud 1-20
for i in range(1,21):
    print(i, end=" ")










print(f"Suvaline arv: {random.randint(1, 20)}")










# Genereeri ja kuva 20 suvalist arvu vahemikus 1-99

for i in range(20):
 print(random.randint(1, 100), end= " ")
 print()








# Kasuta loendit 60, 5, 4, 42, 99, 67, 47, 22, 34, 8, 85, 50, 94, 39, 54, 83, 27, 40, 17, 75
# Leia paaris ja paaritud arvud ning lisa oma loendisse
# Kuva paaris ja paritute arvude summad
loend = [60, 5, 4, 42, 99, 67, 47, 22, 34, 8, 85, 50, 94, 39, 54, 83, 27, 40, 17, 75]
paaris = []
paaritud = []
for i in loend:
   if i%2==0:
      paaris.append(i)
   else:
      paaritud.append(i)

   print(f"Paaris arvude summa: {sum(paaris)}")
   print(f"Paaritute arvude summa: {sum(paairtud)}")


# Kuva arvud 1-42
# Arvud, mis jagunevad 3, lisa tekst TIK (näiteks 3 TIK)
# Arvud, mis jagunevad 5, lisa tekst TAK (näiteks 5 TAK)
# Kui jagunevad mõlemaga, siis lisa tekst TIKTAK (näiteks 15 TIKTAK)
for i in range(1,43):
   if i%3==0:
      print("tiktak", end=" ")
   elif i%5==0:
     print(i, "TAK", end=" ")
   elif i%3==0:
      print(i"TIK", end=" ")
   else:
      print(i, "TIK", end=" ")

print()
# Leia kõik arvud vahemikus 200 kuni 320, mis jaguvad 7-ga, kuid ei jagu 5-ga. Prindi need arvud komadega eraldatult ühele reale.
for i in range(200,321):
   if i%7==0 and i%5>0:
      print(i, end=",")





# Kuva nimekirjast unikaalsed nimed:
nimed = ['Martin', 'Tõnu', 'Andres', 'Tõnu', 'Andres', 'Andres', 'Andres', 'Tõnu', 'Marko', 'Mari', 'Jüri', 'Liis', 'Marko', 'Piret', 'Anu']
unikaalse_nimed = []

for nimi in nimed:
   if nimi in unikaalse_nimed:
      unikaalse_nimed.append(nimi)


for nimi in unikaalse_nimed:
   print(nimi)

#Sulle on saadetud õpilaste keskmised hinded, mille lisasid loendisse. Eralda hinded ning leia kogu rühma parim ja kehvem tulemus ning keskmine hinne.
ryhma_hinded = ["Mari 4.9", "Jüri 3.1", "Kadri 4.6", "Marko 4.7", "Liis 4.9", "Andres 4.2", "Anu 4.7", "Martin 4.2", "Piret 4.2", "Tõnu 4.1"]

for i in ryhma_hinded:
   print(float(i.split(" ")[1]))


print(f"Parim tulemus {max(hinded)}")
print(f"Halvim tulemus {min(hinded)}")
print(f"Keskmine tulemus {sum(hinded)/len(hinded)}")





#Koosta programm, mis genereerib ja kuvab korrutustabeli, kus iga number korrutatakse iseendaga:
#Näiteks:
#0 x 0 = 0
#1 x 1 = 1
#2 x 2 = 4
#3 x 3 = 9
#4 x 4 = 16
#5 x 5 = 25
#6 x 6 = 36
#7 x 7 = 49
#8 x 8 = 64
#9 x 9 = 81
#10 x 10 = 100

for i in range(11):
   print(f"{i} x {i} = {i*i}")




#Loo programm, mis loob suvalised tehted 1-100 arvudega.
#Kasuta tsükli puhul alakriipsu
#kasuta suvalise tehte märgi jaoks loendit ja sealt suvalise märgi leidmiseks random.choice()
#Näiteks:
["7 – 2= 45 * 69= 71 – 45= 84 / 57= 59 * 87= 84 – 71= 65 * 32= 63 – 11= 72 – 90= 29 / 93= "]
tehted = ['+','-','*','/']
for i in range(11):
   i = random.randint(1,100)
   j = random.randint(1,100)
   tehe = random.choice(tehted)
   if tehe=="+":
      print(f"{i} {tehe} {j} = {i+j}")
      vastus = int(input("vastus: "))
      if vastus==i+j
      print("Õige")
      punktid+1=
   elif tehe=="-":
       print(f"{i} {tehe} {j} = {i-j}")
       if vastus==i-j
       print("Õige")
       punktid+1=
   elif tehe=="*":
      print(f"{i} {tehe} {j} = {i*j}")
      if vastus==i*j
      print("Õige")
      punktid+1=
else:
      print(f"{i} {tehe} {j} = {round(i/j,2)}")
if vastus==i/j
print("Õige")
punktid+1=
print()
#Täienda eelmist ülesannet ja kasutaja käest küsitakse vastust.
#Õiged vastused loetakse kokku
#Kui saab vähemalt poole punktid, siis saab A, muul juhul MA



ev_data = [
['vehicle', 'range', 'price'],
['Tesla Model Y Long Range', '330', '58990'],
['Volkswagen ID.4 Pro', '260', '39995'],
['Ford Mustang Mach-E', '300', '42995'],
['Audi e-tron GT', '238', '102700'],
['Nissan Leaf', '149', '27400'],
['BMW iX xDrive50', '324', '83995'],
['Polestar 2', '265', '45500'],
['Kia EV6 Long Range', '310', '47795'],
['Mercedes-Benz EQS 450+', '350', '102310'],
['Hyundai Kona Electric', '258', '37400']
]
 
keskmineOdo = []
KeskmineHind = []

for i in ev_data:
   if i[0] != "vehicle":
      keskmineOdo.append(int(i[1]))
      KeskmineHind.append(int(i[2]))

   #print(i[1])
if i[1] > 300:
   print(i[0])
print(ev_data[1][0]+" "+ev_data[1][1])

print(sum(keskmineOdo)/len(keskmineOdo))
print(sum(KeskmineHind)/len(KeskmineHind))

