# Escribe un programa que muestre por consola (con un print) los
# números de 1 a 100 (ambos incluidos y con un salto de línea entre
# cada impresión), sustituyendo los siguientes:
# Múltiplos de 3 por la palabra "fizz".
# Múltiplos de 5 por la palabra "buzz".
# Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

import numpy as np

nums = np.arange(1, 100)


def  function(nums):
    for i in range(len(nums)):
        if (nums[i] % 3 == 0):
            print("fizz")
        else: 
            if (nums[i] % 5 == 0):
                print("buzz")
            
        
function(nums)
