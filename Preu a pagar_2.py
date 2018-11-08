#coding:utf-8
#Autora: Sofía
#Preu a pagar_2.py
#Tenim: edat, sexe, (H/D), cabells (rossa, morena, pelroja).
#- Els jubilats no paguen.
#- Els homes no jubilats paguen 1€.
#- Les dones no jubilades rosses no paguen, les altres paguen 0,15€

edad = int(input("Escribe tu edad: "))
if ( edad <=5) or (edad >= 65 ):
    print("Gratis")
else:
    if (sexo=="H") and (edad <=65):
        print("Pagar 1€")
    else:
        if (sexo==D) and if (pelo=="R"):
            print("Gratis")
        else:
            print("Pagar: 0,15")

print("2,15€")
