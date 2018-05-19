#  Created by Bogdan Trif on 11-02-2018 , 7:52 PM.
# Polynomials in python
import numpy as np

ppar = [4, 3, -2, 10]
p = np.poly1d(ppar)
print('Evaluate polynomial with value x = 3 : ',p(3))

print(np.polyval(ppar, 3))

x = 3
print(4*x**3 + 3*x**2 -2*x + 10)