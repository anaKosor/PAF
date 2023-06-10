import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.pyplot as plt
import Projectile as p
Pe=p.Projectile(45,10,1,0.01,0.5)
xe,ye=Pe.plot('Euler')
Prk=p.Projectile(45,10,1,0.01,0.5)
xrk,yrk=Prk.plot('Runge-Kutta')
plt.plot(xe,ye,label = "Euler")
plt.plot(xrk,yrk,label = "Runge-Kutta")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
