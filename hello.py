import math

print('Hello world')
x1=int(input('Upišite prvu x kordinatu 1. tocke'))
y1=int(input('Upišite prvu y kordinatu 1. tocke'))
x2=int(input('Upišite prvu x kordinatu 2. tocke'))
y2=int(input('Upišite prvu y kordinatu 2. tocke'))
if x2==x1:
    print('krivi unos')
a=(y2-y1)/(x2-x1)
b=y2-x2*a
print('y={}x+{}'.format(a,b))

print("ovo je vježba")