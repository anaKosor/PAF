import matplotlib.pyplot as plt
import numpy as np

class Sustav:
    def __init__(self, masa1, masa2, polozaj1=(0, 0), polozaj2=(0, 0), brzina1=(0, 0), brzina2=(0, 0), korak_vremena=1):
        self.masa1 = masa1
        self.masa2 = masa2
        self.polozaj1 = np.array(polozaj1)
        self.polozaj2 = np.array(polozaj2)
        self.brzina1 = np.array(brzina1)
        self.brzina2 = np.array(brzina2)
        self.korak_vremena = korak_vremena * 24 * 60 * 60 #dan u s
        self.polozaji1 = []
        self.polozaji2 = []
        self.g = -9.81
        self.G = 6.67 * (10**(-11)) #gravitacijska konstanta
        
    def interakcija(self, trajanje):
        trajanje = trajanje * 24 * 60 * 60
        broj_koraka = int(trajanje / self.korak_vremena)

        for i in range(broj_koraka):
            a1 = (-self.G * self.masa2 / (np.linalg.norm(self.polozaj1 - self.polozaj2)**3)) * (self.polozaj1 - self.polozaj2)
            self.brzina1 = self.brzina1 + a1 * self.korak_vremena
            self.polozaj1 = self.polozaj1 + self.brzina1 * self.korak_vremena
            self.polozaji1.append(self.polozaj1)
            
            a2 = (-self.G * self.masa1 / (np.linalg.norm(self.polozaj2 - self.polozaj1)**3)) * (self.polozaj2 - self.polozaj1) #np.linalg.norm omogućuje izračunavanje Euklidske norme vektora ili matrice(tj.funkcija za izračunavanje duljine vektora)
            self.brzina2 = self.brzina2 + a2 * self.korak_vremena
            self.polozaj2 = self.polozaj2 + self.brzina2 * self.korak_vremena
            self.polozaji2.append(self.polozaj2)
        
        return np.array(self.polozaji1), np.array(self.polozaji2)

t = 365.242
masaZemlje = 5.9742 * 10**24
udaljZemlje = (1.486*10**11, 0) #rz to au
brzinZemlje = (0, 29783) #vz
masaSunca = 1.989 * 10**30 #masaa sunca
udaljSunca = (0,0) 
brzSunca = (0,0)
S1 = Sustav(masaZemlje, masaSunca, udaljZemlje, udaljSunca, brzinZemlje, brzSunca, 1)

z, s = S1.interakcija(t)
for i in range(len(z)):
    plt.plot(z[i, 0], z[i, 1],'b.') #'b.' (crtanje plavih točaka),'yo' označava žute točke

for i in range(len(s)):
    plt.plot(s[i, 0], s[i, 1],'yo')

plt.xlabel('X')
plt.ylabel('Y')
plt.legend(["Zemlja", "Sunce"])
plt.show()

