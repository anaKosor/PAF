import numpy as np
import matplotlib.pyplot as plt
import harmonic_oscillator as hs
#Koristeći razvijeni modul nacrtajte x − t, v − t i a − t graf za neke proizvoljno odabrane početne parametre
x=hs.HarmonicOscillator(1,7,2,1)
x.Euler(4)
x.plot()
