import numpy as np
import matplotlib.pyplot as plt
import math
def derivacija_i_aritmerikaSredina(N): #gdje je N broj točaka koji čemo upisati i izačunati derivaije i aritmetičku sredinu
    lista_y=[]
    lista_x=[]
    for i in range(N):
        x=int(input('koordinada x: ')) #za upisat N x-koordinata
        lista_x.append(x)
        y=int(input('koordinata y :')) #za upisat N y-koordinata
        lista_y.append(y)
    #plt.scatter(lista_x,lista_y) možemo vidjet graf toga ako želimo
    i=0
    sumaX=0
    while i<N:
        sumaX=sumaX + lista_x[i] 
        i=i+1
    aritmetička_sredina=sumaX/len(lista_x)
    
    o=0
    sumaD=0
    while o<N:
        d=(lista_x[o]-sumaX)*(lista_x[o]-sumaX)
        sumaD=sumaD + d
        o=o+1
    derivacija= math.sqrt(sumaD/len(lista_x*(len(lista_x)-1)))
    print('Derivacija iznosi:{}.Aritmetička sredina iznosi: {}'.format(derivacija,aritmetička_sredina))

