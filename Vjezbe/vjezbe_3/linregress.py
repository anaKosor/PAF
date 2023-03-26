import numpy as np
import matplotlib.pyplot as plt
import math
import statistics

M = [0.052, 0.124, 0.168, 0.236, 0.284, 0.336] # y vrijednost
φ= [0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472] # x vrijednost

def mean_xy(lista1,lista2,len):
    lista_xy=[]
    i=0
    while i<len:
        xy=lista1[i]*lista2[i]
        lista_xy.append(xy)
        i=i+1
    return statistics.mean(lista_xy)
mean__xy=mean_xy(M,φ,len(M))

def mean_kvadrat(lista,len_liste):#funkcija za izračunavanje srednje vrijednosti liste (xˇ2)
    i=0
    lista_i=[]
    while i<len_liste:
        x2=lista[i]*lista[i]
        lista_i.append(x2)
        i=i+1
    return statistics.mean(lista_i)

mean_xˇ2=mean_kvadrat(φ,len(φ)) #sredja vrijednost liste xˇ2

a=mean__xy/mean_xˇ2 # koficijent a

mean_yˇ2=mean_kvadrat(M,len(M)) #srednja vrijednost liste yˇ2(tj.M)

greska=math.sqrt(1/len(M)*((mean_yˇ2/mean_xˇ2)-a*a))
os_y=a*np.array([0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472])
plt.scatter(φ,M,color = 'green')
plt.plot(φ,os_y,color='red')
plt.show()
