import numpy as np
import matplotlib.pyplot as plt
import math

class Projectile:
    def __init__(self,kut,v0,m,dt,C=0.2,A=0.1,p=1.293,x=0,y=0): #m-masa tijela,vo-pocetna brzina,kut,x0,y0-pocetni polozaj,dt
        self.kut=kut
        self.p=p #p(phi)-gustoća medija(zrak)
        self.C=C #C(Cd)-koeficijent trenja
        self.A=A #A-površina tijela okomita na smjer gibanja
        self.m=m
        self.v0=v0
        self.vx=v0*math.cos(self.kut)
        self.vy=v0*math.sin(self.kut)
        self.x=x
        self.y=y
        self.dt=dt
        self.lista_x=[]
        self.lista_y=[]

    def plot(self,metoda):
        if metoda=='Euler':
            while self.y>=0:
                ax=-np.sign(self.vx)*((self.p*self.C*self.A)/(2*self.m))*(self.vx*self.vx)
                self.vx=self.vx+ax*self.dt
                self.x=self.x+self.vx*self.dt
                self.lista_x.append(self.x)
                ay=-9.81-np.sign(self.vy)*((self.p*self.C*self.A)/2*self.m)*(self.vy*self.vy)
                self.vy=self.vy+ay*self.dt
                self.y=self.y+self.vy*self.dt
                self.lista_y.append(self.y)
            return self.lista_x,self.lista_y
        elif metoda=='Runge-Kutta':
            while self.y>=0:
                k1vx = -np.sign(self.vx) * ((self.p * self.C * self.A) / (2 * self.m)) * (self.vx * self.vx)*self.dt
                k1vy = -9.81 - np.sign(self.vy) * ((self.p * self.C * self.A) / (2 * self.m)) * (self.vy * self.vy)*self.dt
                k1x = self.vx*self.dt
                k1y = self.vy*self.dt

                k2vx = -np.sign(self.vx+(k1vx/2)) * ((self.p * self.C * self.A) / (2 * self.m)) * ((self.vx+(k1vx/2))*(self.vx+(k1vx/2)))*self.dt
                k2vy = -9.81 - np.sign(self.vy+(k1vy/2)) * ((self.p * self.C * self.A) / (2 * self.m)) * (self.vy+(k1vy/2) * (self.vy+(k1vy/2)))*self.dt
                k2x = (self.vx + (k1vx/2))*self.dt 
                k2y = (self.vy + (k1vy/2)) * self.dt

           
                k3vx = -np.sign(self.vx+(k2vx/2)) * ((self.p * self.C * self.A) / (2 * self.m)) * ((self.vx+(k2vx/2))*(self.vx+(k2vx/2)))*self.dt
                k3vy = -9.81 - np.sign(self.vy+(k2vy/2)) * ((self.p * self.C * self.A) / (2 * self.m)) * (self.vy+(k2vy/2)*(self.vy+(k2vy/2)))*self.dt
                k3x = (self.vx+(k2vx/2))*self.dt
                k3y =(self.vy+(k2vy/2))*self.dt 

                k4vx = -np.sign(self.vx+(k3vx/2)) * ((self.p * self.C * self.A) / (2 * self.m)) * (self.vx+(k3vx/2)*(self.vx+(k3vx/2)))*self.dt
                k4vy = -9.81 - np.sign(self.vy+(k3vy/2)) * ((self.p * self.C * self.A) / (2 * self.m)) * ((self.vy+(k3vy/2))*(self.vy+(k3vy/2)))*self.dt
                k4x = (self.vx + (k3vx/2)) * self.dt
                k4y = (self.vy + (k3vy/2)) * self.dt
            
                ax = (k1vx + 2 * k2vx + 2 * k3vx + k4vx) / 6
                ay = (k1vy + 2 * k2vy + 2 * k3vy + k4vy) / 6

            
                self.vx = self.vx + ax * self.dt
                self.vy = self.vy + ay * self.dt
                self.x = self.x + self.vx * self.dt
                self.lista_x.append(self.x)
                self.y = self.y + self.vy * self.dt
                self.lista_y.append(self.y)

            return self.lista_x,self.lista_y
       


    

    
    



    