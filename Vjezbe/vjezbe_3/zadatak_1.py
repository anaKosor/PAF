a= 5.0 - 4.935
print(a) # očekujem rezultat 0.065, dobiveni rezultat je 0.06500000000000039
#ljudi koriste sustav s bazom 10(sve brojeve zapišemo s zamenkama 0-9),
# a računala koriste binarni sustav s bazom 2(0 i 1) 
# #samo razlomke oblika 1/2**n možemo zapisati u konačnoj binarnoj formi,svi ostali su aproksimacije
# ⇒Računalo ne može točno prikazati brojeve kao 0.1,0.2,0.3…
# stoga će  npr. 0.1 zaokružiti na najbliži broj u tom formatu,
# što će rezultirati malom pogreškom zaokruživanja( čak i prije nego što se izračun dogodi)
b=0.1+0.2+0.3 #python float rezervira 64 bita 
if b==0.6:
    print('rezultat je 0.6')
else:
    print(b)
 
 
 
 

