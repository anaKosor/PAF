#napravit funkciju koja ulazne parametre prima funkciju i točku(bit ce potrebno i dx i koja metodu zeli koristit)
import matplotlib.pyplot as plt
import numpy as np

def derivacija23(funkcija,x,dx,metoda=3): # prva metoda ,metoda ce uvjek biti 3 osim ako se bas ne zapise kao parametar 2
    if metoda=='3':
        d=(( funkcija(x + dx) - funkcija(x - dx) ) / (2 * dx) )
        return d
    else: #metoda=='2'
        d=((funkcija(x + dx) - funkcija(x)) / (dx))
        return d
#rderivacija kao ulazne parametre funkciju i gornju i donju granicu raspona derivacije
def derivacije(funkcija,gornja,donja,dx,metoda=3): 
    tocke = np.arange(donja, gornja, dx)
    list=[]
    if metoda=='3':
        for i in tocke:
            list.append(derivacija23(funkcija,i,dx))
    else:
        for i in tocke:
            list.append(derivacija23(funkcija,i,dx,2))
    return tocke, list

# pravokutnu aproksimacija integrala(bitno da za gornju beđu poceti od 2.clana[1],a za donju od 1.tj[0])gornja(= f(x1)Δx + f(x2)Δx + ⋯ + f(xn)Δx)
def pintegral(funkcija,donja, gornja,dx):
    tockeL=[]      #lista tocaka za donju medu
    donjameda=[]   #i tu ce biti lista tocaka od donje sume( f(x1)Δx + f(x2)Δx + ⋯ + f(xn)Δx))
    tockeU=[]      #lista tocaka za gornju medu
    gornjameda=[]  # lista tocaka od gornje sume gornja(= f(x1)Δx + f(x2)Δx + ⋯ + f(xn)Δx))
    gornja_suma = 0
    donja_suma = 0

    while donja<= gornja:
        tockeL.append(donja)
        donja_suma=donja_suma + funkcija(donja)*dx
        donjameda.append(donja_suma)#za listu tih donjih vrijednosti a moglo se i koristiti np.arrey(donja,gornja,dx)
        donja =donja +dx #i kako za donju pocinje od od 1. clana a za gornju od 2. gornjnu medu racunamo posli uvjeta, za se donja povecava za dx dok ne bude >=od gornje
        tockeU.append(donja)
        gornja_suma=gornja_suma+function(donja)*dx
        gornjameda.append(gornja_suma)
    return tockeL,tockeU,gornjameda,donjameda

def integral_trapez(f,donja,gornja,n):
    list=np.linspace(donja,gornja,n+1)
    x=(gornja-donja)/n
    int=0
    for i in range(n):
        int+=x*(f(list[i])+f(list[i+1]))/2
    return integral




        
    






