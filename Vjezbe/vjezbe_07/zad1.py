import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.pyplot as plt
import Projectile as p

x1=p.Projectile(45,10,0.1,0.1)
x1,y1=x1.Euler()
x2=p.Projectile(45,10,0.1,0.001)
x2,y2=x2.Euler()
x3=p.Projectile(45,10,0.1,0.05)
x3,y3=x3.Euler()
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.plot(x3,y3)
plt.xlabel("x")
plt.ylabel("y")
plt.show()