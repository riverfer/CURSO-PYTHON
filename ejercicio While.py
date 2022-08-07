# -*- coding: utf-8 -*-
# EJERCICIO WHILE

#contar=input("Ingrese el # al que debo contar: ")
#contar=int(contar)

#------------------------EJERCICIOS WHILE
contar=5
contador=1
while contador<=contar:
    print(contador)
    contador=contador+1
    
#----------------------------------------------------------------------------
contar=5
contador=1
while contador<=contar:
    print(contador, end="")
    contador=contador+1    
  
#--------------#OTRA FORMA DE INCREMENTAR UNA VARIABLE------------------------
contar=5
contador=1
while contador<=contar:
    print(contador, end="")
    contador +=1    
    
#----------------WHILE CON BREAK-----------------------------------------------
contar=5
contador=1
while True:
    print(contador, end="")
    contador+=1
    if contador>contar:
        break