import random

# 1. Genereeri ja kuva arvud 1-20
arvud_1_20 = list(range(1, 21))
print("Arvud 1-20:", arvud_1_20)

# 2. Genereeri ja kuva 20 suvalist arvu vahemikus 1-99
suvalised_arvud = [random.randint(1, 99) for _ in range(20)]
print("20 suvalist arvu 1-99 vahemikus:", suvalised_arvud)

# 3. Kasuta etteantud loendit
arvud = [60, 5, 4, 42, 99, 67, 47, 22, 34, 8, 85, 50, 94, 39, 54, 83, 27, 40, 17, 75]

# 4. Leia paaris ja paaritud arvud
paarisarvud = []
paaritudarvud = []

for arv in arvud:
    if arv % 2 == 0:
        paarisarvud.append(arv)
    else:
        paaritudarvud.append(arv)

print("Paarisarvud:", paarisarvud)
print("Paaritud arvud:", paaritudarvud)

# 5. Summa arvutused
summa_paaris = sum(paarisarvud)
summa_paaritud = sum(paaritudarvud)

print(f"Paarisarvude summa: {summa_paaris}")
print(f"Paaritute arvude summa: {summa_paaritud}")

# 1. Kuva arvud 1-42 ja lisa TIK, TAK või TIKTAK
print("1–42 koos TIK/TAK märgetega:")
for i in range(1, 43):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i} TIKTAK")
    elif i % 3 == 0:
        print(f"{i} TIK")
    elif i % 5 == 0:
        print(f"{i} TAK")
    else:
        print(i)

print("\n---\n")

# 2. Leia arvud vahemikus 200–320, mis jaguvad 7-ga, aga mitte 5-ga
sobivad_arvud = [str(x) for x in range(200, 321) if x % 7 == 0 and x % 5 != 0]
print("Arvud vahemikus 200-320, mis jagunevad 7-ga, aga mitte 5-ga:")
print(", ".join(sobivad_arvud))

print("\n---\n")

# 3. Kuva nimekirjast unikaalsed nimed
nimed = ['Martin', 'Tõnu', 'Andres', 'Tõnu', 'Andres', 'Andres', 'Andres',
         'Tõnu', 'Marko', 'Mari', 'Jüri', 'Liis', 'Marko', 'Piret', 'Anu']

unikaalsed_nimed = list(set(nimed))
print("Unikaalsed nimed:")
print(unikaalsed_nimed)
ryhma_hinded = ["Mari 4.9", "Jüri 3.1", "Kadri 4.6", "Marko 4.7", "Liis 4.9",
                "Andres 4.2", "Anu 4.7", "Martin 4.2", "Piret 4.2", "Tõnu 4.1"]

# Hinded eraldatakse ja teisendatakse float-tüüpi numbriteks
hinded = [float(rida.split()[1]) for rida in ryhma_hinded]

parim = max(hinded)
kehvem = min(hinded)
keskmine = sum(hinded) / len(hinded)

print(f"Parim hinne: {parim}") 
print(f"Kehvim hinne: {kehvem}")
print(f"Keskmine hinne: {keskmine:.2f}")
# Korrutustabel
print("\nKorrutustabel (0–10):")
for i in range(0, 11):
    print(f"{i} x {i} = {i * i}")
    
märgid = ["+", "-", "*", "/"]

oiged = 0  # Õigete vastuste arv

for _ in range(10):
    arv1 = random.randint(1, 100)
    arv2 = random.randint(1, 100)
    märk = random.choice(märgid)

    # Vältime nulliga jagamist
    if märk == "/" and arv2 == 0:
        arv2 = 1

    # Koosta tehe ja kuva kasutajale
    tehe = f"{arv1} {märk} {arv2}"
    kasutaja_vastus = input(f"{tehe} = ")

    try:
        # Arvuta õige vastus
        if märk == "+":
            tulemus = arv1 + arv2
        elif märk == "-":
            tulemus = arv1 - arv2
        elif märk == "*":
            tulemus = arv1 * arv2
        elif märk == "/":
            tulemus = round(arv1 / arv2, 2)  # Ümardame 2 kohta

        # Kontrolli, kas kasutaja vastas õigesti (ka ümardus)
        if abs(float(kasutaja_vastus) - tulemus) < 0.01:
            print("Õige!")
            oiged += 1
        else:
            print(f"Vale! Õige vastus oli: {tulemus}")

    except:
        print("Vigane sisend!")

# Tulemus
print(f"\nÕigeid vastuseid: {oiged}/10")

if oiged >= 5:
    print("Hinne: A")
else:
    print("Hinne: MA")

# Kahanev tärnide rida
for i in range(5, 0, -1):
    print("*" * i)
    
print()
for i in range(1, 6):
    print(" " * (5 - i) + "*" * i)
    
print()
for i in range(1, 6):
    print(" " * (i - 5) + "*" * i)

print()
for i in range(5):
    print(" " * i + "*" * (5 - i))

even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 3, 32, 34, 36, 38]

summa = 0
for arv in even_nums:
    if arv % 2 != 0:
        print(f"Leiti paaritu arv: {arv}. Tsükkel katkestatakse.")
        break
    summa += arv
else:
    print("Tsükkel jõudis lõpuni.")

print(f"Paarisarvude summa: {summa}")

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

# Tabeli kuvamine
print(f"{'Vehicle':35} {'Range (km)':>10} {'Price ($)':>10}")
print("-" * 60)
for row in ev_data[1:]:
    print(f"{row[0]:35} {row[1]:>10} {row[2]:>10}")

total_range = 0
total_price = 0
for row in ev_data[1:]:
    total_range += int(row[1])
    total_price += int(row[2])

average_range = total_range / (len(ev_data) - 1)
average_price = total_price / (len(ev_data) - 1)

print(f"\nKeskmine läbisõit: {average_range:.1f} km")
print(f"Keskmine hind: ${average_price:.2f}")

print("\nAutod, mille läbisõit on üle 300 km:")
for row in ev_data[1:]:
    if int(row[1]) > 300:
        print(f"- {row[0]} ({row[1]} km)")

high_price_ranges = []
low_price_ranges = []

# Jagame autod kaheks grupiks, piiriks keskmine hind
for row in ev_data[1:]:
    price = int(row[2])
    car_range = int(row[1])
    if price > average_price:
        high_price_ranges.append(car_range)
    else:
        low_price_ranges.append(car_range)

avg_high_price_range = sum(high_price_ranges) / len(high_price_ranges)
avg_low_price_range = sum(low_price_ranges) / len(low_price_ranges)

print(f"\nKeskmine läbisõit kallitel autodel: {avg_high_price_range:.1f} km")
print(f"Keskmine läbisõit odavamatel autodel: {avg_low_price_range:.1f} km")

if avg_high_price_range > avg_low_price_range:
    print("📈 Kallimatel autodel on keskmiselt pikem sõiduulatus.")
else:
    print("📉 Kallimatel autodel ei ole keskmiselt pikemat sõiduulatust.")
