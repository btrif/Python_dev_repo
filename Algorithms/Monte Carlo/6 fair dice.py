#  Created by Bogdan Trif on 13-09-2017 , 11:13 AM.

import random

print( random.randint(1 , 6)  )

nr_of_rolls = 100000
S = 0
for i in range( nr_of_rolls  ) :
    r = random.randint(1 , 6)
    S += r
    # print(r)

print('Expected Value after ', nr_of_rolls , '  rolls =  ',  S/nr_of_rolls )