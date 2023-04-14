import paricle as pt
import numpy as np
import matplotlib.pyplot as plt
import math
p=pt.Particle(10,60,0,0)
ndomet=[]
adomet=[]

def analiticki_domet(v0,kut,x0,y0):
    kut_radiani=kut*(math.pi/180)
    ay=-9.81 
    vx= v0 *math.cos(kut_radiani) 
    vy= v0 *math.sin(kut_radiani)
    t=-2*vy/ay
    return x0 +vx*t

dt=0
while dt<=0.2:
    ad=analiticki_domet(10,60,0,0)
    Numericki_domet=p.domet(dt)
    ndomet.append(Numericki_domet)
    adomet.append(ad)
    dt=dt+0.0001

greska=[]
i=0
while i<len(ndomet):
    erorr=100*abs(adomet[i]-ndomet[i])/adomet[i]
    greska.append(erorr)
    i=i+1

vrijeme=list(range(0,0.2,0.0001))

print(len(ndomet))