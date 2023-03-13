import numpy as np
import matplotlib.pyplot as plt
import math
v0=100
kut=int(45)
kut_radiani=kut*(math.pi/180) # program ne moze  u stupnjevima,te treba pretvorit u radiane
ay=-9.8  #vertikalna komponenta akceleracije(vertikalna sila je gravitacija)
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
while y>=0:
    lista_vremena.append(t)
    vx=vx+ax*0.01
    lista_vx.append(vx)
    vy=vy+ay*0.01
    lista_vy.append(vy)
    x=x + vx*0.01
    lista_x.append(x)
    y=y + vy*0.01
    lista_y.append(y)
    t=t+0.01
    

plt.plot(lista_x,lista_y)
plt.show()
 
 



