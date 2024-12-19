#1
#from random import randint 

#for i in range (1,11):
#    num1 = randint (1,10)
#    num2 = randint (1,10)
#    print ("Küsimus",i,":",num1,"*",num2,"=", end = " ")
#    guess = int (input())
#    answer = num1*num2
#    if guess == answer:
#        print ("Õige!")
#    else:
#        print ("Vale. Vastus on: ",answer)


#2
#teams = [
#[("Joosep",12),("Oliver",13),("Kevin",10),("Laura",11)],
#[("Gregor",12),("Sander",14),("Robin",13)],
#[("Karl",14),("Karolin",10)]
#]



#def age(teams):
#    for team in teams:
#        for member in team:
#           print(member[1])
#
#age(teams)



#7

#def currency_converter(UserInput): 
#    EEK = 8.09647
#    error_message = 'Viga: teie sisend peaks olema positiivne arv'
#    
#    try:
#        EUR = float(UserInput)*EEK
#        print(f"Teie panus on võrdne {EUR} kividega")
#    except:
#        print(error_message)
#
#
#conversion = input('Sisestage väärtus eurodes, mis teisendatakse EEK-i:')
#currency_converter(conversion)



#8
with open('palk.txt', 'r') as file:

    palgad = []

for line in file:

    emp_id, sugu, palk = line.lower().strip().split(",")

s = float(palk)

palgad.append(s)

Keskmine = sum(palgad)/len(palgad)

Keskmine_mees = sum(palgad)/len(palgad)

print("Palgad kokku = ",sum(palgad))

print("Keskmised palgad = ", Keskmine)

print("Keskmise meessoo palgad = ", Keskmine_mees)
