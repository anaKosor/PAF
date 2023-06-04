import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.pyplot as plt
import Projectile as p

x1=p.Projectile(45,10,0.1,0.1)
x1,y1=x1.plot('Euler')
x2=p.Projectile(45,10,0.1,0.0001)
x2,y2=x2.plot('Euler')
x3=p.Projectile(45,10,0.1,0.05)
x3,y3=x3.plot('Euler')
plt.plot(x1,y1,label ='Euler dt=0.1')
plt.plot(x3,y3,label ='Euler dt=0.05')
plt.plot(x2,y2,label ='Euler dt=0.0001')
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()