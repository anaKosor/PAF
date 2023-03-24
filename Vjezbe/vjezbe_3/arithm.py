#a)
import numpy as np
import matplotlib.pyplot as plt
import math
lista_x=[]
i=0
while i<10: #prvo napisati koordinate svih 10 točki te posebno sastaviti listu x , y koordinata
    x=int(input('koordinada x: ')) #za upisat 10 x-koordinata
    lista_x.append(x)
    i=i+1

sumaX=0
p=0
while p<10:
    sumaX=sumaX + lista_x[p] #svaki sljedeci u listi(index tog člana od 0-9) ćemo dodavati /zbrajati dok ne dobijemo sumu svih njih zajedno
    p=p+1

aritmetička_sredina=sumaX/len(lista_x) 
   
   
o=0
d=0

while o<10:
    d= d + (lista_x[o]-aritmetička_sredina)*(lista_x[o]-aritmetička_sredina) #sada kao i kore uzimamo 1. član pa se petlja ponovi pa  2. .....
    o=o+1

deviacija= math.sqrt(d/len(lista_x*(len(lista_x)-1)))
print('Deviacija iznosi:{}.Aritmetička sredina iznosi: {}'.format(deviacija,aritmetička_sredina))


