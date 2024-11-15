# 22.10.24 Rasmus
# Ülesanne 7 Massiivid


# Muusikapalad
laulud = ['ALIKA – "Bridges" ']


,Anett x Fredi – "Read Between The Lines" '] ,villemdrillem – "leekiv armastus" '] ,Clicherik & Mäx – "PAKSUD" '] ,nublu – "ära ärata" '] ,NOËP – "Move Your Feet" '] ,Trad.Attack! – "Bring It On" '] ,Bedwetters – "It Is What It Is" '] ,Reket– "Panama paberid" '] ,Grete Paia – "Võluväel" ']


for i in range(10):
    print(str(i+1)+". ")
try:
    valik = int(input("Vali lugu 1-10: "))
    print(f"Mängin: {laulud[valik-1]}")
except:
    print("Tegid vale otsuse :)")



# Astaajad

[('jaanuar'-2;-8;-4;-27;1;-11;-8;-12;-27;5;-22;4;4;-5;7;-15;1;-8;-29;2;-28;-23;-18;-9;-18;-22;-19;0;-23;5;-4) ('veebruar'-4;-25;-20;8;-23;-27;3;-3;-19;-10;-15;-17;-5;-14;-21;-24;-3;-24;-28;-18;-14;-25;-15;-25;7;1;-27;10;-18;-22;-6) ('märts'-1;8;-3;-13;3;-12;-29;-23;-24;-14;5;-15;-8;-10;-23;-30;-14;9;-4;-16;-19;10;-11;-28;-25;-11;-2;-9;-10;-21;-16) ('aprill'-12;-21;-5;0;-13;-28;-13;-7;-16;9;-4;-18;-23;8;8;-23;9;5;-5;-11;-25;-8;-9;-8;-23;-3;-20;-12;-10;-23;1) ('mai'5;-15;-5;-9;-3;-1;-26;-29;-3;-6;-18;1;-10;-6;-7;9;7;4;7;6;-21;-1;-16;-25;-27;-8;-29;10;-1;-26;-25) ('juuni'-22;-3;-22;-7;-15;-7;-7;-12;-24;-25;-17;0;-12;-27;10;-21;-13;-27;-9;-27;0;-4;-23;-7;-20;7;-8;-16;-5;-19;-20) ('juuli'-1'-17;-13;-14;-18;-30;-29;-23;-9;3;-16;-8;7;7;9;-23;9;-5;-27;-22;-27;-26;-27;-7;3;6;-8;-5;-20;-15;2) ('august'-11'-3;-17;-4;7;-7;2;-9;2;-21;7;4;-21;-17;-12;-29;-9;2;-19;-5;-30;-12;-9;-10;-17;0;-9;-5;6;-13;9) ('september'-21;-10;4;-12;-19;-25;-30;-27;4;1;4;-29;-13;-26;0;10;-29;-12;6;-12;-14;-30;-16;-16;-8;-28;-24;-21;1;-7;0) ('oktoober'-16;7;8;-12;-11;3;2;-22;5;-14;0;4;-30;-21;-21;-20;-22;-24;-25;-22;-19;-10;0;-13;1;-1;-26;-28;-25;-15;-14) ('november'8;6;-28;10;-6;1;-26;-2;-7;-16;-6;-18;3;-24;0;-5;-23;-15;-24;9;-9;5;-11;6;-5;-1;10;-9;-3;-10;-17) ('detsember'-10;-23;2;-3;-27;1;-4;-11;-5;-14;3;6;-13;-27;-23;7;-23;-11;-21;-23;-19;1;-25;5;-16;9;-16;3;-20;-9;-6)]

print(f"Hetkekuu {kuud[9][0]}")
kuus_kokku = len(kuud[9])-1
print(F"Viimane mõõtmine: {kuud[9][kuus_kokku]}")
print("Selle kuu temperatuurid:")
for i in range(kuus_kokku):
    ajutine.append(kuud[9][i+1], end=",")
    print(kuud[9][i], end=" ,")
print()
print(f"Max temp: {max(kuud[9])}")
print(f"Min temp: {min(kuud[9])}")
print(f"Keskmine temp: {round(sum(ajutine)/len(ajutine),2)}")
print(f-20 esineb {ajutine.count(-20)} korda")



ajutine.del(5-1)
#del.ajutine[4]
ajutine.insert(5-1,16)
ajutine.sort()
print(ajutine)

