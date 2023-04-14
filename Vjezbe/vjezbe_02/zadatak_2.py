import numpy as np
import matplotlib.pyplot as plt
import math
v0=100
kut=45
kut_radiani=kut*(math.pi/180) # program ne moze  u stupnjevima,te treba pretvorit u radiane
ay=-9.81  #vertikalna komponenta akceleracije(vertikalna sila je gravitacija)
ax=0     #horizontalna komponenta akceleracije(brzina je stalna)
vx= v0 *math.cos(kut_radiani) #horizontalna kom.brzine pocetne brzine
vy= v0 *math.sin(kut_radiani)#veritkalna komp.brzine ppocetne brzine
lista_vx=[]
lista_vy=[]
lista_x=[]
lista_y=[]
lista_vremena=[]
x=0
y=0 #pocetak gibanja je u (0,0) ishodištu
t=0
dt=0.01
while t<=10:
    lista_vremena.append(t)
    vx=vx+ax*dt
    lista_vx.append(vx)
    vy=vy+ay*dt
    lista_vy.append(vy)
    x=x + vx*dt
    lista_x.append(x)
    y=y + vy*dt
    lista_y.append(y)
    t=t+dt
    


plt.subplot(1,3,1)
plt.plot(lista_x, lista_y) #x-y graf
 

plt.subplot(1,3,2)
plt.plot(lista_vremena, lista_x)#x-t graf


plt.subplot(1,3,3)
plt.plot(lista_vremena, lista_y)#y-t graf
plt.show()

 
 



