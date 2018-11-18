#coding:utf-8
#Autora: Sofía
#Fecha creación: 15/11/18
#Ejercicio_leer_numeros_4.py
"""EJERCICIO 2 
Leer 3 números y mostrar el mayor
*******************************************************************"""

print("Leer 3 números y mostrar el mayor")
num1 = 0
num2 = 0
num3 = 0
num1 = int(input("Escribe un número: "))
num2 = int(input("Escribe un número: "))
num3 = int(input("Escribe un número: "))

if (num3 > num1) and (num3 > num2):
            print ("Es mayor el número tres: " + str(num3))

else:
       if num1 > num2 :
        print("El mayor el número uno:  " + str(num1))
       else:
        if num2 > num1 :
                  print("Es mayor el número dos:  " + str(num2))
