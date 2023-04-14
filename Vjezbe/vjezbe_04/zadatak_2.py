import paricle as pt
import numpy as np
import matplotlib.pyplot as plt
import math

ndomet=[]
adomet=[]

def analiticki_domet(v0,kut,x0,y0):
    kut_radiani=kut*(math.pi/180)
    ay=-9.81 
    vx= v0 *math.cos(kut_radiani) 
    vy= v0 *math.sin(kut_radiani)
    t=-2*vy/ay
    return x0 +vx*t

ad=analiticki_domet(10,60,0,0)

i=0.0001
while i<=0.1:
    adomet.append(ad)
    i=i+0.0001

p=pt.Particle(10,60,0,0)

t=0.0001
while t<=0.1:
    t=t+0.0001
    nd=p.domet(t)
    ndomet.append(nd)
    print(ndomet)
    

erorr=100*abs(np.array(adomet)-np.array(ndomet))/np.array(adomet)

time=[]
z=0.0001
while z<=0.1:
    time.append(z)
    z=z+0.0001
