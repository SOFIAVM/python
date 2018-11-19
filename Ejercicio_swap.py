#coding:utf-8
#Autora: Sofía
#Fecha creación: 15/11/18
#Ejercicio_swap.py
"""SWAP. Intercambio de variables
mano_der=”movil”
mano_izq=”bocadillo”
Pista: Usar una variable temporal “mano_extra”
Ejercicio_swap.py"""

mano_der="movil" 
mano_izq="bocadillo"
print("Muestra que tiene cada mano antes del intercambio de variable: ")
print("La mano derecha tiene el: "+str(mano_der))
print("La mano izquierda tiene el: "+str(mano_izq))
mano_extra="mano_der" #->"movil" 
mano_der="mano_izq"   #->"bocadillo"
mano_izq="mano_extra" #->"movil"

#Variables después del intercambio:
mano_extra="mano_der" #->"nada"
mano_der= "bocadillo" #"mano_der"(así no imprime el valor "bocadillo")   #->"bocadillo"
mano_izq= "movil"     #"mano_izq"(así no imprime el valor "movil")       #->"movil"
print("Después del intercambio: ")
print("La mano derecha tiene el: "+str(mano_der))
print("La mano izquierda tiene el: "+str(mano_izq))



