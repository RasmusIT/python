import json

# Ava fail ja lae sisu JSON kujul
with open("C:\\Users\\User\\Desktop\\quotes.txt", "r", encoding="utf-8") as f:
    data = json.load(f)  # json.load(f) – loeb faili sisu ja teisendab selle automaatselt Python andmestruktuuriks (sõnastikuks ja listiks).

quotes = data["quotes"]  # võtame ainult tsitaatide loendi

# Küsi kasutajalt otsingusõna
otsi = input("Sisesta otsingusõna (autori nimi või tsitaadi osa): ").strip().lower() #strip() – eemaldab algusest ja lõpust tühikud.
                                                                                    #lower() – muudab sisendi väiketähtedeks, et otsing oleks tähtede suurusest sõltumatu (case-insensitive).

# Otsime vasted
tulemused = [
    q for q in quotes
    if otsi in q["quote"].lower() or otsi in q["author"].lower()  #Käib läbi kõik tsitaadid listis quotes ja lisab need, mille tsitaadis (q["quote"]) või autori nimes (q["author"]) leidub otsingusõna otsi.
]

# Kuva tulemused
if tulemused: #Kui tulemused pole tühi (leiti vähemalt üks vaste), siis täidame järgmist plokki.
    print("\nLeitud tsitaadid:")
    for q in tulemused[:5]:  # maksimaalselt 5 esimest tulemust
        print(f"{q['id']}. {q['author']}: \"{q['quote']}\"") #f"...{q['id']}..." – kasutame f-stringi, et vormindada tsitaadi ID, autor ja tsitaat ilusasti ühele real
else:
    print("Tulemusi ei leitud.") #Kui tulemused on tühi list ([]), kuvatakse teade, et midagi ei leitud.
