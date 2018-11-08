# coding: utf​-8
#Autora: Sofía 
#Fecha creación: 07/11/18
#Ejercicio: comparador-años.py
#Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos
#años han pasado desde ese año o cuántos años faltan para llegar a ese año.
#COMPARADOR DE AÑOS:
#¡En qué año estamos?: 2018
#Escriba un año cualquiera: 2020
#Para llegar al año 2020 faltan 2 años
#COMPARADOR DE AÑOS:
#¡En qué año estamos?: 2018
#Escriba un año cualquiera: 1997
#Desde el año 1997 han pasado 21 años
#COMPARADOR DE AÑOS:
#¡En qué año estamos?: 2018
#Escriba un año cualquiera: 2018
#¡Son el mismo año!

anyo_actual = int(input("¿En qué año estamos?: "))
anyo_cualquiera = int(input("Escribe un año cualquiera: "))

if ( anyo_actual == 0) and  (anyo_cualquiera == 0) :
    print("Error")
else:
        if ( anyo_actual == 0) and  (anyo_cualquiera > 0) :
            print("Error")
        else:
                if ( anyo_actual > 0)  and  (anyo_cualquiera == 0) :
                    print("Error")
                else:
                        if ( anyo_actual == anyo_cualquiera ) :
                            print("¡Son el mismo año!")
                        else:
                                if ( anyo_actual < anyo_cualquiera ) :
                                    print("Para llegar al año " + str(anyo_cualquiera), "falta/n: " + str(anyo_cualquiera - anyo_actual), "años")
                                else:
                                        if ( anyo_actual >  anyo_cualquiera  ) :
                                            print("¡Desde el año " + str (anyo_cualquiera), "han pasado: " + str(anyo_actual -  anyo_cualquiera), "años")
                                        
                                                                                 
