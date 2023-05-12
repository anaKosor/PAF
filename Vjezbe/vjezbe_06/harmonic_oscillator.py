import numpy as np
import matplotlib.pyplot as plt
#Napišite modul "harmonic_oscillator.py" koji će sadržavati klasu HarmonicOscillator s raznim metodama
#potrebnim za opis gibanja jednostavnog harmoničkog oscilatora u jednoj dimenziji
class HarmonicOscillator:
    def __init__(self, m, k, x0, v0, dt=0.01): #masa, konstanta , početni položaj i brzinu
        self.m = m
        self.k = k
        self.x0 = x0
        self.v0 = v0
        self.dt = dt
        self.acceleration = []
        self.position = []
        self.velocity = []
        self.time = []

    def Euler(self, t): #kositi Euler-ovu metodu za izračun ubrzanja,brzinu,položaj oscilatora za zadano vrijeme t
        time = np.arange(0, t, self.dt)
        for t0 in time:
            acceleration = -(self.k/self.m) * self.x0
            self.acceleration.append(acceleration)
            self.v0 = self.v0 + acceleration * self.dt
            self.velocity.append(self.v0)
            self.x0 = self.x0 + self.v0 * self.dt
            self.position.append(self.x0)
            self.time.append(t0)
        return self.acceleration, self.velocity, self.position, self.time 
        
    def plot(self): #kao sto je u zad 1 napisano metoda za plotanje x-t,v-t,a-t grafova
        plt.subplot(1,3,1)
        plt.title("x-t")
        plt.plot(self.time,self.position)
        plt.subplot(1,3,2)
        plt.title("v-t")
        plt.plot(self.time,self.velocity)
        plt.subplot(1,3,3)
        plt.title("a-t")
        plt.plot(self.time,self.acceleration)
        plt.show()

    def analytical_graph(self, t): #racuna analitički za položaj oscilatora da mi ga mogli posli usporedit s numerickim 
        time = np.arange(0, t, self.dt)
        omega = np.sqrt(self.k / self.m)
        amplitude = np.sqrt(self.x0 ** 2 + (self.v0 / omega) ** 2)
        if self.x0 == 0:
            if self.v0 > 0:
                p = 0.5 * np.pi
            else:
                p = -0.5 * np.pi
        else:
            p = np.arctan(-self.v0 / (omega * self.x0))
        position = amplitude * np.cos(omega * time + p)
        return position, time
