import numpy as np

ar = np.linspace(1, 100, 10)
print(ar)

def sum(ar):
    suma = 0
    for i in ar:
        suma += i
    print("la suma es", suma)
   
    
sum(ar)