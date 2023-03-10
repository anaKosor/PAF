#zadatak 4
def pravac(x3,y3,x4,y4):
    a=int((y4-y3)/(x4-x3))
    b=y4-x4*a
    return a,b
y=pravac(-1,3,3,-1)

if y[0]==0:
    print('y={}'.format(y[1]))
elif y[1]==0:
    print('y={}x'.format(y[0]))
elif y[1]<0:
    print('y={}x {}'.format(y[0],y[1]))
else:
    print('y={}x+{}'.format(y[0],y[1]))