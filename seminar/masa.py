import numpy as np
import matplotlib.pyplot as plt
import math
import seminar as s
#ovisnost o masi 
projektil1=s.Projectile(1,0.5)
x1,y1=projektil1.plot()
projektil2=s.Projectile(5,0.5)
x2,y2=projektil2.plot()
projektil3=s.Projectile(10,0.5)
x3,y3=projektil3.plot()
a=[x1[-1],x2[-1],x3[-1]]
print(a)
sort=sorted(a)
print(sort)
plt.plot(x1,y1,c='black',label ='m=1')
plt.plot(x2,y2,c='blue',label='m=5')
plt.plot(x3,y3,c='red',label = 'm=10')
plt.xlabel("x[m]")
plt.ylabel("y[m]")
plt.legend()
plt.show()
