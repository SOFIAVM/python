#coding:utf-8
#Autora: Sofía
#Fecha creación: 15/11/18
#Ejercicio_leer_numeros_5.py
""" EJERCICIO 3
Leer 4 números y mostrar el mayor
*****************************************************************"""

print("Leer 4 números y mostrar el mayor")
num1 = 0
num2 = 0
num3 = 0
num4 = 0
num1 = int(input("Escribe un número: "))
num2 = int(input("Escribe un número: "))
num3 = int(input("Escribe un número: "))
num4 = int(input("Escribe un número: "))


if (num4 > num1) and (num4 > num2) and (num4 > num3):
            print ("Es mayor el número cuatro: " + str(num4))

else:
    if (num3 > num1) and (num3 > num2):
        print ("Es mayor el número tres: " + str(num3))
    else:
        if num1 > num2 :
            print("El mayor el número uno:  " + str(num1))
        else:
            if num2 > num1 :
                print("Es mayor el número dos:  " + str(num2))
    
