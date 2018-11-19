#coding:utf-8
#Autora: Sofía
#Fecha creación: 15/11/18
#Ejercicio_swap_4.py
"""SWAP. Intercambio de cajones
Antes:                                             Después:
cajon1="movil”                                     cajon1="boli"
cajon2=”bocadillo”                                 cajon2="bebida"
cajon3="boli"                                      cajon3="movil"
cajon4="bebida"                                    cajon4="bocadillo"
Usaré las variables:
"cajon_extra_1" y "cajon_extra_2"""

cajon1="movil"
cajon2="bocadillo"
cajon3="boli"
cajon4="bebida"  

print("Muestra el contenido de los cajones antes del intercambio: ")
print("El cajón 1 tiene: "+str(cajon1))
print("El cajón 2 tiene: "+str(cajon2))
print("El cajón 3 tiene: "+str(cajon3))
print("El cajón 4 tiene: "+str(cajon4))

#Intercambio de cajones:
cajon_extra_1="cajon1" #->"movil" 
cajon1="cajon3"        #->"boli"  OK CAJON 1
cajon3="cajon_extra_1" #->"movil"  OK CAJON 3
cajon_extra_1="cajon4" #->"bebida"
cajon_extra_2="cajon2" #->"bocadillo" 
cajon2="cajon_extra_1" #->"bebida" OK CAJON 2
cajon4="cajon_extra_2" #->"bocadillo" OK CAJON 4


"""
DESPUÉS
cajon1="boli"
cajon2="bebida"
cajon3="movil"
cajon4="bocadillo"""

#Cajones después del intercambio:
print("Después del intercambio de cajones: ")
print("El cajón 1 tiene: "+str(cajon1))
print("El cajón 2 tiene: "+str(cajon2))
print("El cajón 3 tiene: "+str(cajon3))
print("El cajón 4 tiene: "+str(cajon4))

#Valor final de cada cajón:
cajon_extra_1="cajon1" #->"movil" 
cajon1="boli"        #->"boli"  OK CAJON 1
cajon3="movil" #->"movil"  OK CAJON 3
cajon_extra_1="cajon4" #->"bebida"
cajon_extra_2="cajon2" #->"bocadillo" 
cajon2="bebida" #->"bebida" OK CAJON 2
cajon4="bocadillo" #->"bocadillo" OK CAJON 4



print("Mostrando el contenido final de los cajones:")
print("El cajón 1 tiene: "+str(cajon1))
print("El cajón 2 tiene: "+str(cajon2))
print("El cajón 3 tiene: "+str(cajon3))
print("El cajón 4 tiene: "+str(cajon4))