import matplotlib.pyplot as plt
import numpy as np
F=float(input('unesite silu: '))
m=float(input('unesite masu cestice(kg): '))

a = float(F / m)
lista_akc=[]
t = 0
lista_vremena = []
while t < 10:
    lista_vremena.append(t)
    lista_akc.append(a)
    t = t + 0.01

plt.plot(lista_vremena, lista_akc)
plt.show()