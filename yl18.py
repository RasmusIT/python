import csv

faili_nimi = 'EstonianBasketballGames.csv'

with open (faili_nimi, mode='r', encoding='utf-8') as fail:
    csv_lugeja = csv.reader(fail)
    
    pais = next(csv_lugeja)
    
    print(f"Päise veerud: {pais}")
    for rida in csv_lugeja:
        print(rida)

        