# coding: utf8
#Autora: Sofía 
#Fecha creación: 19/11/18
#Ejercicio_pares.py
#Lee un número del teclado
#Si es par: Escribe “Qué bonito número par”
#Si es impar: Escribe “Qué número más vulgar”
#Pista: usar módulo %

numero = int(input("Introduce un número: "))
if (numero % 2 == 0) :    # (numero % 2 == 0)<---Si es  un nº par
    print("Qué bonito número par")

else:
     print("Qué número más vulgar")