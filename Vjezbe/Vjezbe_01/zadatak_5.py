import matplotlib.pyplot as plt

def pravac(x3,y3,x4,y4):
    x_values = [x3,x4]
    y_values = [y3,y4]
    s=plt.plot(x_values,y_values)
    upit=input('pdf ili prikaz na ekranu: ')
    if upit=='pdf':
        plt.savefig('zadatak_5'+'.pdf')
    else:
        plt.show()
        return s
pravac(1,2,3,4)
        
    
