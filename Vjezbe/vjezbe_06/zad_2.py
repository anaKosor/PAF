import numpy as np
import matplotlib.pyplot as plt
import harmonic_oscillator as hs

h1=hs.HarmonicOscillator(1,7,2,1,0.01)
a1, v1, x1, t1 = h1.Euler(4)
h2=hs.HarmonicOscillator(1,7,2,1,0.02)
a2, v2, x2, t2 = h2.Euler(4)
h3=hs.HarmonicOscillator(1,7,2,1,0.05)
x3,t3=h3.analytical_graph(4)
plt.scatter(t1,x1,s=4) #s je velicina tockica(fontsize=4)
plt.scatter(t2,x2,s=4)
plt.plot(t3,x3,linewidth=1)
plt.show()
