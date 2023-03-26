import numpy as np
import matplotlib.pyplot as plt
import math
import statistics

M = [0.052, 0.124, 0.168, 0.236, 0.284, 0.336] # y vrijednost
φ= [0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472] # x vrijednost


# treba napraviti prvo liste umnoska x,y pa nihovu prosjecnu vrijednost
#napraviti listu x^2 i njigovu prosječnu vrijednost za koficijent a
i=0
lista_xy=[]
while i<(len(φ)):
    xy=φ[i]*M[i]
    lista_xy.append(xy)
    i=i+1
mean_xy=statistics.mean(lista_xy)
print(mean_xy)
def mean_kvadrat(lista,len_liste):#funkcija za izračunavanje srednje vrijednosti liste (xˇ2)
    i=0
    lista_i=[]
    while i<len_liste:
        x2=lista[i]*lista[i]
        lista_i.append(x2)
        i=i+1
    return statistics.mean(lista_i)
mean_xˇ2=mean_kvadrat(φ,len(φ))

a=mean_xy/mean_xˇ2 # koficijent a

mean_yˇ2=mean_kvadrat(M,len(M))
greska=math.sqrt(1/len(M)*((mean_yˇ2/mean_xˇ2)-a*a))

print(mean_kvadrat(φ,len(φ)))
print(lista_xy,mean_xy,mean_xˇ2,a)
