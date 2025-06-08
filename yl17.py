with open('C:\\Users\\User\\Desktop\\pangakonto.txt', 'r',encoding='utf-8') as f:
    read=f.readlines()  #open(...) avab faili nimega pangakonto.txt lugemiseks ('r').

                        #encoding='utf-8' – toetab täpitähti ja rahvusvahelisi sümboleid.

                        #with hoolitseb, et fail suletakse automaatselt pärast lugemist.

                        #f.readlines() loeb kogu faili sisu ja salvestab read listi, kus iga element on üks rida tekstina.
 #  Initsialiseerime muutujad, millesse hakkame tehingute andmeid koguma:

#kogu_tehingud: mitu rida (tehingut) failis on

#positiivsed_arv: mitu tehingut olid positiivsed (sissetulek)

#positiivsed_summa: kui suur on positiivsete tehingute kogusumma             
                
kogu_tehingud=0
positiivsed_arv=0
positiivsed_summa=0.0
#Töötleme iga rida ehk iga tehingut

for rida in read:
    try:
        summa=float(rida.strip()) #eemaldame tühikud ja teisendame float'iks
        kogu_tehingud+=1  #Iga edukalt läbitud tehingu korral suurendame tehingute koguarvu
        if summa>0:                    #Kui summaon suurem kui null siis:
            positiivsed_arv+=1         #suurendame positiivsete tegingute arvu
            positiivsed_summa+=summa    #liidame selle summa positiivsele kogusummale
    except ValueError:                  #Kui mingi rida ei saa float’iks teisendada (nt tekst või tühi rida), siis:
        continue                        #tekib ValueError
                                         #continue tähendab, et jätkame järgmise reaga
print(f"Kogu tehingute arv:{kogu_tehingud}")
print(f"Positiivsete tehingute arv: {positiivsed_arv}")
print(f"Positiivsete tehingute kogusumma: {positiivsed_summa:.2f} €")


with open('C:\\Users\\User\\Desktop\\palgad.txt', 'r', encoding='utf-8') as f:
    read=f.readlines()
# Meeste ja naiste statistika hoidmiseks
mehed_tasu = 0
mehed_tunnid = 0
mehed_palk = 0
mehed_arv = 0

naised_tasu = 0
naised_tunnid = 0
naised_palk = 0
naised_arv = 0

# Läbime iga rea
for rida in read:
    try:
        andmed = rida.strip().split(',') 
        #rida.strip() eemaldab rea algusest ja lõpust kõik tühikud ja reavahetuse.
        #.split(',') jagab rea koma põhjal eraldi osadeks (listi).
        sugu = andmed[3].strip().lower()
        #sugu on 4. veerg (index 3), teisendame selle väikesteks tähtedeks, et võrdlused oleks lihtsamad.
        tasu = float(andmed[4])
        tunnid = float(andmed[5])
        palk = float(andmed[6])
        #tas (tunnitasu), tunnid (töötundide arv) ja palk teisendame komaarvudeks (float).

        if sugu == 'mees':  #Kui sugu on mees, lisame meeste summadesse tunnitasu, tunnid,
                                      #palga ja suurendame meeste arvu ühe võrra.
                                       #Kui sugu on naine, teeme sama naiste muutujatega.
            mehed_tasu += tasu
            mehed_tunnid += tunnid
            mehed_palk += palk
            mehed_arv += 1
        elif sugu == 'naine':
            naised_tasu += tasu
            naised_tunnid += tunnid
            naised_palk += palk
            naised_arv += 1
    except:
        continue  # Kui mõni rida on vigane, jätame selle vahele

# Arvutame keskmised
def keskmine(kogusumma, arv):
    return kogusumma / arv if arv > 0 else 0 #Defineerime väikese abifunktsiooni, mis arvutab keskmise, vältides nulliga jagamist.

# Meeste keskmised
m_keskm_tasu = keskmine(mehed_tasu, mehed_arv)
m_keskm_tunnid = keskmine(mehed_tunnid, mehed_arv)
m_keskm_palk = keskmine(mehed_palk, mehed_arv)

# Naiste keskmised
n_keskm_tasu = keskmine(naised_tasu, naised_arv)
n_keskm_tunnid = keskmine(naised_tunnid, naised_arv)
n_keskm_palk = keskmine(naised_palk, naised_arv)

# Väljund konsooli
print("MEESTE STATISTIKA:")
print(f"- Keskmine tunnitasu: {m_keskm_tasu:.2f} €")
print(f"- Keskmine töötundide arv: {m_keskm_tunnid:.1f}")
print(f"- Keskmine palk: {m_keskm_palk:.2f} €\n")

print("NAISTE STATISTIKA:")
print(f"- Keskmine tunnitasu: {n_keskm_tasu:.2f} €")
print(f"- Keskmine töötundide arv: {n_keskm_tunnid:.1f}")
print(f"- Keskmine palk: {n_keskm_palk:.2f} €")