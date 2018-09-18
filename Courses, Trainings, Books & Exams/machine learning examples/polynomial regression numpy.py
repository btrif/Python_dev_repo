#  Created by Bogdan Trif on 09-02-2018 , 10:16 PM.

# polynomial regression using python


import numpy as np

x = np.array([0.0, 1.0, 2.0, 3.0,  4.0,  5.0])
y = np.array([0.0, 0.8, 0.9, 0.1, -0.8, -1.0])
z = np.polyfit( x, y, 3)


print('z : \t', z)

print('\n----------------------------------------')
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.polyfit.html

import matplotlib.pyplot as plt

p = np.poly1d(z)
print('p(0.5) = ', p(0.5))
print('p(3.5) = ', p(3.5))
print('p(10) = ', p(10))

p30 = np.poly1d(np.polyfit(x, y, 30))

print('p30(4) = ', p(4))
print('p30(5) = ', p(5))
print('p30(4.5) = ', p(4.5))

xp = np.linspace(-2, 6, 100)
_ = plt.plot(x, y, '.', xp, p(xp), '-', xp, p30(xp), '--')
plt.ylim(-2,2)

plt.show()