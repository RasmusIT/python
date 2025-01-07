#6
#a = 0
#
#while a == 0:
#    print("\n \n" * 100)
#    print("Sisestage sõna, et kontrollida, kas see on palindroom: ")
#    word = input("?: ")
#
#    wordLength = int(len(word))
#    finalWordLength = int(wordLength / 2)
#    firstHalf = word[:finalWordLength]
#    secondHalf = word[finalWordLength + 1:]
#    secondHalf = secondHalf[::-1]
#    print(firstHalf)
#    print(secondHalf)
#
#    if firstHalf == secondHalf:
#        print("See on palindroom")
#    else:
#        print("See ei ole palindroom")
#
#
#    print("taaskäivitamiseks vajutage sisestusklahvi")
#    input()


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




#10
def enter_score ():
    results = []
    scores = int(input("Sisestage Tulemuste arv : "))
    for i in range(scores):
        student_name = input("Sisestage nimi: ")
        student_score = int(input("Sisestage Tulemuste skoor " + student_name + " : " ))        
        results.append((student_name, student_score))
        print(results)
    return results

def calc_average(results):
    total=0
    for student_name, student_score in results:
        total=total+student_score
    average= total/len(results)
    print("keskmime skoor on ", average)
    return average

def above_average(results, average_score):
    above_average_no=0
    for student_name, student_score in results:
        if student_score > average_score:
            above_average_no = above_average_no + 1
            print(" kõige parim skoor on ", above_average_no)
    return above_average_no

results = enter_score()
average_score = calc_average(results)

above_average_no = above_average(results, average_score)
