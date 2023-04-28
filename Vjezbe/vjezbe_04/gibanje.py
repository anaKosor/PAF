import paricle as pt
import numpy as np
import matplotlib.pyplot as plt
import math

p1=pt.Particle(10,45,0,0)

Numericki_domet=p1.domet(0.001)

def analiticki_domet(v0,kut,x0,y0):
    kut_radiani=kut*(math.pi/180)
    ay=-9.81 
    vx= v0 *math.cos(kut_radiani) 
    vy= v0 *math.sin(kut_radiani)
    t=-2*vy/ay
    return x0 +vx*t

print(analiticki_domet(10,45,0,0),Numericki_domet)