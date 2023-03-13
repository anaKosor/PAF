import matplotlib.pyplot as plt
import numpy as np
F=float(input('unesite silu: '))
m=float(input('unesite masu cestice(kg): '))

a = float(F / m)

lista_akc=[]
lista_vremena = []
lista_brzina = []
lista_pomaka = []
t = 0
v=0
x=0
t0 = 0.01


while t <= 10:
    v = v + a*t0
    x = x + v*t0
    lista_vremena.append(t)
    lista_brzina.append(v)
    lista_pomaka.append(x)
    lista_akc.append(a) # a-t graf
    t = t + t0




plt.subplot(1,3,1)
plt.plot(lista_vremena, lista_akc)
 

plt.subplot(1,3,2)
plt.plot(lista_vremena, lista_brzina)


plt.subplot(1,3,3)
plt.plot(lista_vremena, lista_pomaka)
plt.show()
