import matplotlib.pyplot as plt
import calculus as cl
import numpy as np

#iz prezentacije uzimamo 5x**3-2x**2+2x-3 i ta df 15x**2-4x+2
def funkcija(x):
    return 5*x**3-2*x**2+2*x-3
def deriviranaf(x):
    return 15*x**2-4*x+2
#popzvat cemo iz ir calsulus da izracuna raspon al za na razlicina epsilona tj.dx(0.1 i 0.01)
#iz prezentacije iscitamo  da ce gornja biti -1 a donja 2
E1=cl.raspon_derivacije(funkcija,gornja,donja,dx=0.1) #koristi se metoda 3 al ako zelimo metodu 2 cl.raspon_derivacije(funkcija,gornja,donja,dx=0.1,2)
E2=cl.raspon_derivacije(funkcija,gornja,donja,dx=0.01) 

