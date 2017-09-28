#  Created by Bogdan Trif on 07-09-2017 , 9:28 PM.
'''
Suppose you live in a city where the streets are straight , perpendicular , they form squares or blocks
You decide to go for a walk and you can go N, S, E, W at each intersection.
Once you are finished with your walk, you check how far away you are from central point (0, 0 )
If you are more than 4 block away, you pay for a taxi back home, otherwise you just walk.

QUESTION : What is the longest random walk you can take so that  ON AVERAGE
you will end up 4 block or fewer from home ?
there is less than 50 % chance that you will pay for taxi back home.

MONTE CARLO Simulation

'''

import random

def random_walk(n):
    ''' Return coordinates after  n block random walks'''
    x , y = 0 , 0
    for i in range(n) :
        ( dx, dy ) = random.choice([(1, 0) ,(-1, 0) ,(0,1) ,(0,-1)  ])
        x += dx
        y += dy
    return (x, y)

# for i in range(25) :
#     walk = random_walk(10)
#     print(walk, '   Distance from home  = ', abs( walk[0] ) + abs( walk[1] ) )

# monte Carlo math approach, We conduct thousand of random trials, you compute
# the percentage of random walk that end in a short walk home.
number_of_walks = 10000

# Let's estimate the probability that you will walk home for lengths from 1-30
for walk_length in range(1, 31) :
    no_transport = 0        # counter, Number of walks 4 blocks or fewer from home
    for i in range(number_of_walks) :
        (x , y ) = random_walk(walk_length)
        distance = abs(x) + abs(y)
        if distance <= 4 :
            no_transport +=1
    no_transport_percentage = float(no_transport) / number_of_walks
    print('Walk size = ', walk_length , ' / % of no transport  = ' , 100*no_transport_percentage )
