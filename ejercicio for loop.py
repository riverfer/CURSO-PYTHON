# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 18:07:55 2022

@author: fernando.rivera
"""

#                                EJERCICIO FOR LOOP
for item in range(10,0,-1):
    print (item)
#-----------------------------------------------------------------------------
for item in range(10):
        print (item)
#-----------------------------------------------------------------------------     
Lista= ["R1",
        "R2",
        "R3",
        "R4",
        "S1",
        "S2",
        "S3",]
print(Lista)
#------------------------------------------------------------------------------
Lista= ["R1",
        "R2",
        "R3",
        "R4",
        "S1",
        "S2",
        "S3",]
        
for item in Lista:
    print(item, end="*")
    
#-----------------------------------------------------------------------------

Lista= ["R1",
        "R2",
        "R3",
        "R4",
        "S1",
        "S2",
        "S3",]
        
for item in Lista:
    if "R" in item:
        print(item, end=" ")

 #---------------------------------------------------------------------------   
Lista1=[]
Lista= ["R1","R2","R3","R4","S1","S2","S3"]
         
for item in Lista:
    if "R" in item:
         Lista1.append(item)
print(Lista1)
 
 #----------------------------------------------------------------------------

Lista1=[]
Lista2=[]
Lista= ["R1","R2","R3","R4","S1","S2","S3"]
          
for item in Lista:
     if "S" in item:
          Lista1.append(item)
     else:
         Lista2.append(item)     
print(Lista1, Lista2)
 
 
 