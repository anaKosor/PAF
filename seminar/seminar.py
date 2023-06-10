import matplotlib.pyplot as plt
import numpy as np

class Projectile:
    
    def __init__(self, mass,C, v0=10, x0=0, y0=0, phi=45, rho=1.2, A=0.1, dt = 0.001):
        self.dt = dt
        self.mass = mass
        self.phi = (phi / 180) * np.pi
        self.vx = v0 * np.cos(self.phi)
        self.vy = v0 * np.sin(self.phi)
        self.x0 = x0
        self.y0 = y0
        self.rho = rho
        self.C = C
        self.A = A
        self.list_x  = []
        self.list_y  = []
        

    
    
    def plot(self): #metoda za plot koristeci runge-kutta metodu 4.reda
        g = 9.81
        
        while self.y0 >= 0:
            k1vx = (- np.sign(self.vx) * ((self.rho * self.C * self.A) / (2 * self.mass)) * (self.vx)**2) * self.dt
            k1x = self.vx * self.dt
            k2vx = (- np.sign(self.vx + (k1vx / 2)) * ((self.rho * self.C * self.A) / (2 * self.mass))* (self.vx + (k1vx / 2))**2) * self.dt
            k2x = (self.vx + (k1vx / 2)) * self.dt
            k3vx = (- np.sign(self.vx + (k2vx / 2)) * ((self.rho * self.C * self.A) / (2 * self.mass)) * (self.vx + (k2vx / 2))**2) * self.dt
            k3x = (self.vx + (k2vx / 2)) * self.dt
            k4vx = (- np.sign(self.vx + (k3vx / 2)) * ((self.rho * self.C * self.A) / (2 * self.mass)) * (self.vx + (k3vx / 2))**2) * self.dt
            k4x = (self.vx + (k3vx / 2)) * self.dt
            
            self.vx += (1/6) * (k1vx + 2*k2vx + 2*k3vx + k4vx)
            self.x0 += (1/6) * (k1x + 2*k2x + 2*k3x + k4x)
            
            k1vy = (- g - np.sign(self.vy) * ((self.rho * self.C * self.A) / (2 * self.mass)) * (self.vy)**2) * self.dt
            k1y = self.vy * self.dt
            k2vy = (- g - np.sign(self.vy + (k1vy / 2)) * ((self.rho * self.C * self.A) / (2 * self.mass)) * (self.vy + (k1vy / 2))**2) * self.dt
            k2y = (self.vy + (k1vy / 2)) * self.dt
            k3vy = (- g - np.sign(self.vy + (k2vy / 2)) * ((self.rho * self.C * self.A) / (2 * self.mass)) * (self.vy + (k2vy / 2))**2) * self.dt
            k3y = (self.vy + (k2vy / 2)) * self.dt
            k4vy = (- g - np.sign(self.vy + (k3vy / 2)) * ((self.rho * self.C * self.A) / (2 * self.mass)) * (self.vy + (k3vy / 2))**2) * self.dt
            k4y = (self.vy + (k3vy / 2)) * self.dt
            
            self.vy += (1/6) * (k1vy + 2*k2vy + 2*k3vy + k4vy)
            self.y0 += (1/6) * (k1y + 2*k2y + 2*k3y + k4y)
            
           
            self.list_x.append(self.x0)
            self.list_y.append(self.y0)
            
            
        return self.list_x, self.list_y
    

