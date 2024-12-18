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

def currency_converter():
    conversion = input('Sisestage väärtus eurodes, mis teisendatakse eekideks:')
    EEK = 8.09647
    error_message = 'Viga: teie sisend peaks olema positiivne arv'

    if (conversion.isdigit() == False):
        return(error_message)
    elif (conversion.isdecimal() == False):
        return (error_message)
    else:
        conversion = float(conversion) * EEK
        print("Teie sisend on võrdne {output} stones".format(output=conversion))
        return conversion