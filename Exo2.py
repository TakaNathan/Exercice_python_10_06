#Fonction qui recupere la temperature entre par l'utilisateur,
#et affiche une activite en fonction
#(float)->(int)
def choix_activite(temp) :
    if temp >= 80.0 :
        numero_activite = 1
    elif temp >= 60 :
        numero_activite = 2
    elif temp >= 40 :
        numero_activite = 3
    else :
        numero_activite = 4
    return numero_activite

activite = ["Natation","Soccer","Volleyball","Ski"]
temp = float(input("Veuillez entrer la temperature qu'il fait: "))
numero = choix_activite(temp)
print("Activite est :",activite[numero-1])
