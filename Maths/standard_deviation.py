#  Created by Bogdan Trif on 22-05-2018 , 4:36 PM.

### Standard Deviation ( standard deviation )   How do you calculate the standard deviation?
# =   To calculate the standard deviation of those numbers:
# 1.  Work out the Mean (the simple average of the numbers)
# 2.  Then for each number: subtract the Mean and square the result.
# 3.  Then work out the mean of those squared differences.
# 4.  Take the square root of that and we are done!

import numpy as np
x = np.array([2.97, 1.27, 3.72])

def standard_deviation (X) :
    ''':Description: Returns the standard deviation of sequence of numbers
    :param X: lst,
    :return: sigma, standard deviation              '''
    miu = np.mean(X)
    sM = [ (i-miu)**2 for i in X ]
    print('sM : ', sM)
    sigma = (np.mean(sM))**(1/2)
    print('sigma standard deviation = ', sigma )
    return sigma

print('Function Standard deviation :', standard_deviation(x))
print('NUMPY Standard deviation :', np.std(x)  )

