#b)Napišite program pod (a) koristeći gotove module
import numpy as np
import matplotlib.pyplot as plt
import math
import statistics

lista_x=[]
i=0
while i<10:
    x=int(input()) 
    lista_x.append(x)
    i=i+1

aritmeticka=np.mean(lista_x)  #modul za prosječnu vrijednost(na engleskom : arithmetic mean),može se koristit i statistics.mean()
c=statistics.stdev(lista_x)
print(c)
deviacija=(statistics.stdev(lista_x))/math.sqrt((len(lista_x)))
print('Deviacija iznosi: {} ,a arimetička sredina: {}'.format(deviacija,aritmeticka))

#korištenje standardne deviacije modula statistike
#formula koja nam je zadana u pdf prezentacije je preciznija za manju količinu podataka,
# kako su u gotovom modulu statistike formule  malo drugačije(jer se u velikoj količini podataka mogu zanematiri male variacije),
#onada za statistics.stdev( ) treb dodati /math.sqrt(len(liste_brojeva)), a za statistics.pstdev() dodati /math.sqrt(len(lista)-1) ,to su razlike u formulama
