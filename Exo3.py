#Fonction qui va recuperer un entier et retourner un chiffre
#entre 1 et 3 en fonction de sa divisiblilite par 2 et 3
#(float)->(int)
def estDivisible(nombre) :
    if nombre%2==0 and nombre%3==0 :
        resultat_test = 1
    elif nombre%2==0 or nombre%3==0 :
        resultat_test = 2
    else :
        resultat_test = 3
    return(resultat_test)

nombre = float(input("Entrer la valeur à tester: "))
resultat = ["Divisible par 2 et par 3","Divisible par 2 ou par 3","Divisible ni par 2 ni par 3"]
test = estDivisible(nombre)
print(resultat[test-1])
