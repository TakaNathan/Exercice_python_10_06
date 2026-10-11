#Programme qui recupere les coef d'un polynome
#de degre2 ax^2 + bx + c et renvoie son nombre de racines


def discriminant(a,b,c) :
    #fonction qui calcule un discriminant a partir. 3 float
    #(float,float,float)->(float)
    #∆=b^2-4ac
    delta = (b)**2 - 4*(a*c)
    return delta

def nombre_racines(delta) :
    #fonction qui donne un nombre de racines en fonction du signe de ∆
    #(float)->(int)
    if delta>0 :
        nombre_racines = 2
    elif delta ==0 :
        nombre_racines = 1
    else :
        nombre_racines = 0
    return nombre_racines

coef_a = float(input("Entrer le coefficient a de l'equation: "))
coef_b = float(input("Entrer le coefficient b de l'equation: "))
coef_c = float(input("Entrer le coefficient c de l'equation: "))
delta = discriminant(coef_a,coef_b,coef_c)

nombre_racine_reelle = nombre_racines(delta)
print("Le nombre de racines reelles de ce polynome est:",nombre_racine_reelle)




    
    

