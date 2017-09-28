for n in range(2, 16):
     for x in range(2, n):
         if n % x == 0:
             print(n, 'equals', x, '*', n // x)
             break
     else:
         print(n, 'is a prime number')

import os       # needed only for path Print
print(os.path.realpath(__file__))       # Path of the current file