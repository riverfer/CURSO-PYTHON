"""
Created on Sat Aug  6 01:12:15 2022

@author: fernando.rivera
"""
 
def l100kmtompg(valor):
     resultado= (100*1000*3.785411784)/(valor*1609.34)
     print(resultado)
l100kmtompg(3.9)
l100kmtompg(7.5)
l100kmtompg(10.0)
    
def mpgtol100km(valor1):
    resultado1= (100*1000*3.785411784)/(valor1*1609.34)
    print(resultado1)
mpgtol100km(60.3)
mpgtol100km(31.4)
mpgtol100km(23.5)