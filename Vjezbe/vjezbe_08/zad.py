import matplotlib.pyplot as plt
import numpy as np

class Čestica:
    def __init__(self, masa, q, E, B, v0, x0, dt=0.01):
        self.masa = masa
        self.q = q
        self.E = np.array(E)
        self.B = np.array(B)
        self.v0 = np.array(v0)
        self.x0 = np.array(x0, dtype=float) 
        self.dt = dt

    def putanja(self, t):
        t_vrijednosti = np.arange(0.0, t + self.dt, self.dt)
        broj_koraka = len(t_vrijednosti)
        self.x = np.zeros((broj_koraka, 3)) #np.zeros,funkcija koja stvara niz nula određene veličine(stvara metricu velicinje broj koraka*3)

        for i in range(broj_koraka):
            t = t_vrijednosti[i]
            ubrzanje = (self.q / self.masa) * (self.E + np.cross(self.v0, self.B)) #np.cross izračunava vektorski produkt između dva vektora
            self.v0 += ubrzanje * self.dt
            self.x0 += self.v0 * self.dt
            self.x[i] = self.x0

        return self.x
    

E = (0, 0, 0)
B = (0, 0, 1)
v = (0.15, 0.15, 0.15)
x = (0, 0, 0)

p1 = Čestica(0.5, 1, E, B, v, x)
p2 = Čestica(0.5, -1, E, B, v, x)

p = p1.putanja(21)
e = p2.putanja(21)
px = [točka[0] for točka in p]
py = [točka[1] for točka in p]
pz = [točka[2] for točka in p]

ex = [točka[0] for točka in e]
ey = [točka[1] for točka in e]
ez = [točka[2] for točka in e]

graf = plt.axes(projection="3d")
graf.view_init(30, 37)
graf.plot(px, py, pz, label='p+')
graf.plot(ex, ey, ez, label='e-')
graf.legend()
plt.show()