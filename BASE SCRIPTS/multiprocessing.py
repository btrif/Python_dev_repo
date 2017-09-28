import time
from math import sqrt

#######################

t1  = time.time()


[sqrt(i ** 2) for i in range(10**7)]


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')




######################################
t1  = time.time()



from joblib import Parallel, delayed
Parallel(n_jobs=4)(delayed(sqrt)(i ** 2) for i in range(10**7))



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
