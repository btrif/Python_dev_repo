#  Created by Bogdan Trif on 17-05-2018 , 8:27 PM.
# https://en.wikipedia.org/wiki/M%C3%B6bius_function

from math import floor, sqrt

def mobius_sieve(lim):

        mu = [1] * (lim + 1)
        for i in range(2, lim+1):
            if mu[i] == 1:
                for j in range(i, lim+1, i):
                    mu[j] *= -i
                for j in range(i*i, lim+1, i*i):
                    mu[j] = 0
        for i in range(2, lim+1):
            if mu[i] == i:
                mu[i] = 1
            elif mu[i] == -i:
                mu[i] = -1
            elif mu[i] < 0:
                mu[i] = 1
            elif mu[i] > 0:
                mu[i] = -1
        return mu


mob = mobius_sieve(2**8)
print(mob[:100])