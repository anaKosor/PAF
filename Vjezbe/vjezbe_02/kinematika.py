import numpy as np
import matplotlib.pyplot as plt
import math

def jednoliko_gibanje(F,m,T): #ulazni parametri su F(sila,N), m(masa,kg),t(vrijeme gibanja)
    a = float(F / m)
    lista_akc=[]
    lista_vremena = []
    lista_brzina = []
    lista_pomaka = []
    t = 0
    v=0
    x=0
    t0 = 0.01
    while t <= T:
        v = v + a*t0
        x = x + v*t0
        lista_vremena.append(t)
        lista_brzina.append(v)
        lista_pomaka.append(x)
        lista_akc.append(a)
        t = t + t0
    plt.subplot(1,3,1)
    plt.plot(lista_vremena, lista_akc) #a-t graf
    plt.subplot(1,3,2)
    plt.plot(lista_vremena, lista_brzina)#v-t graf
    plt.subplot(1,3,3)
    plt.plot(lista_vremena, lista_pomaka)#x-t graf
    plt.show()

def kosi_hitac(v0,kut,T): # vo(početna brzina), kut(početni kut izbačaja), T(vrijeme kretanja tijela)
    kut_radiani=kut*(math.pi/180)
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
    while t<=T:
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



