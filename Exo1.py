#Recupere l'age entre par l'user et affiche un message
#different si l'age est compris entre 18 et 55 ou pas
#
#Contrat de type : ()->(bool)

def test_age() :
    age = int(input("Entrer l'age que vous souhaitez évaluer: "))
    bool_age = (age>=18 and age<=55)
    return bool_age

if test_age() :
    print("Transaction acceptée!")
else :
    print("Transaction refusée")