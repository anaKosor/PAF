import numpy as np
import matplotlib.pyplot as plt
import math
import seminar as s
#ovisnost o koficijentu trenja sfera(cd=0.47(),kocku(cd=1.05) I aerodinamično tijelo(cd=0.04)
sfera=s.Projectile(1,0.47)
xs,ys=sfera.plot()
kocka=s.Projectile(1,1.05)
xk,yk=kocka.plot()
atijelo=s.Projectile(1,0.04)
xa,ya=atijelo.plot()
a=[xa[-1],xs[-1],xk[-1]]
print(a)
sort=sorted(a)
print(sort)
plt.plot(xa,ya,c='black',label ='CD=0.04')
plt.plot(xs,ys,c='blue',label='CD=0.47')
plt.plot(xk,yk,c='red',label = 'CD=1.05')
plt.xlabel("x[m]")
plt.ylabel("y[m]")
plt.legend()
plt.show()
