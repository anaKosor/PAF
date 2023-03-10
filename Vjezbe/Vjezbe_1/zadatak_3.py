import math
#zadatak 3
x11=input('Upišite prvu x kordinatu 1. tocke: ')
y11=input('Upišite prvu y kordinatu 1. tocke: ')
x21=input('Upišite prvu x kordinatu 2. tocke: ')
y21=input('Upišite prvu y kordinatu 2. tocke: ')

if x11.isdigit() and x21.isdigit() and y11.isdigit() and y21.isdigit():
    if y11==y21 and x11==x21:
        print('Nema pravca,kordinate su iste. Ponovo upišite dvje kordinate!')
    elif y11==y21:
        print('Jednadžba pravca je y={}'.format(y11))
    elif x11==x21:
        print('Jednadžba pravca je x={}'.format(x11))
    else:
        x1=int(x11)
        y1=int(y11)
        x2=int(x21)
        y2=int(y21)
        a=int((y2-y1)/(x2-x1))
        b=y2-x2*a
        if b>=0:
            print('y={}x+{}'.format(a,b))
        else:
            print('y={}x {}'.format(a,b))

else:
    print('Upišite valjanje kordinate!')
