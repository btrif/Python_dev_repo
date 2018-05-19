#  Created by Bogdan Trif on 11-02-2018 , 8:56 PM.

import numpy as np
import matplotlib.pyplot as plt

x = np.array([ 3.08,  3.1 ,  3.12,  3.14,  3.16,  3.18,  3.2 ,  3.22,  3.24,
    3.26,  3.28,  3.3 ,  3.32,  3.34,  3.36,  3.38,  3.4 ,  3.42,
    3.44,  3.46,  3.48,  3.5 ,  3.52,  3.54,  3.56,  3.58,  3.6 ,
    3.62,  3.64,  3.66,  3.68])

y = np.array([ 0.000857,  0.001182,  0.001619,  0.002113,  0.002702,  0.003351,
    0.004062,  0.004754,  0.00546 ,  0.006183,  0.006816,  0.007362,
    0.007844,  0.008207,  0.008474,  0.008541,  0.008539,  0.008445,
    0.008251,  0.007974,  0.007608,  0.007193,  0.006752,  0.006269,
    0.005799,  0.005302,  0.004822,  0.004339,  0.00391 ,  0.003481,
    0.003095])

'''
Unfortunately, np.polynomial.polynomial.polyfit returns the coefficients in the opposite 
order of that for np.polyfit and np.polyval (or, as you used np.poly1d). To illustrate:
'''

print( np.polynomial.polynomial.polyfit(x, y, 4) )
print(np.polyfit(x, y, 4) )


'''
In general: np.polynomial.polynomial.polyfit returns coefficients [A, B, C] to A + Bx + Cx^2 + ..., 
while np.polyfit returns: ... + Ax^2 + Bx + C.

So if you want to use this combination of functions, you must reverse the order of coefficients, as in:
'''

ffit = np.polyval(y[::-1], x)

'''
However, the documentation states clearly to avoid np.polyfit, np.polyval, and np.poly1d, and instead to use only the new(er) package.
You're safest to use only the polynomial package:
'''

import numpy.polynomial.polynomial as poly

coefs = poly.polyfit(x, y, 4)
ffit = poly.polyval(x, coefs)


plt.plot(x, ffit,  'ro-' )
plt.show()




