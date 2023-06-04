import matplotlib.pyplot as plt
import numpy as np

class Čestica:
    def __init__(self, masa, q, E, B, v0, x0, dt=0.01):
        self.masa = masa
        self.q = q
        self.E = np.array(E)
        self.B = np.array(B)
        self.v0 = np.array(v0)
        self.x0 = np.array(x0)
        self.dt = dt

    def putanja(self, t):
        t_vrijednosti = np.arange(0.0, t + self.dt, self.dt)
        broj_koraka = len(t_vrijednosti)
        self.x = np.zeros((broj_koraka, 3))

        for i in range(broj_koraka):
            t = t_vrijednosti[i]
            ubrzanje = (self.q / self.masa) * (self.E + np.cross(self.v0, self.B))
            self.v0 += ubrzanje * self.dt
            self.x0 += self.v0 * self.dt
            self.x[i] = self.x0

        return self.x