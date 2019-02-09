#  Created by Bogdan Trif on 02-02-2019 , 12:07 PM.
import time
'''
https://math.stackexchange.com/questions/889712/the-fastest-way-to-count-prime-number-that-smaller-or-equal-n
https://codegolf.stackexchange.com/questions/74269/calculate-the-number-of-primes-up-to-n
http://am-just-a-nobody.blogspot.com/2015/11/algorithm-for-summing-all-primes-less.html
http://am-just-a-nobody.blogspot.com/2015/09/mathjax_13.html
http://am-just-a-nobody.blogspot.com/2015/11/c-code-for-primepi-function.html
https://en.wikipedia.org/wiki/Prime-counting_function


'''


t1  = time.time()

def main_(x) :

    def Phi(m, b):
        if not b:
            return m
        if not m:
            return 0
        if m >= 800:
            return Phi(m, b - 1) - Phi(m // primes[b - 1], b - 1)
        t = b * 800 + m
        if not Phi_memo[t]:
            Phi_memo[t] =  Phi(m, b - 1) - Phi(m // primes[b - 1], b - 1)
        return Phi_memo[t]



    if x < 6:
        print( [0, 0, 1, 2, 2, 3][x])
        exit()

    root2 = int(x ** (1./2))
    root3 = int(x ** (1./3))
    top = x // root3 + 1
    sieve = [0, 0] + [1] * (top - 2)
    pi = [0, 0]
    primes = []
    t = 0

    for i in range(2, top):
        if sieve[i] == 1:
            t += 1
            primes.append(i)
            sieve[i::i] = [0] * len(sieve[i::i])
        pi.append(t)

    a, b = pi[root3 + 1], pi[root2 + 1]
    Phi_memo = [0] * ((a + 1) * 800)

    print('Up to ' +str(x) +' :  ' ,Phi(x, a) + a - 1 - sum(pi[x // p] - pi[p] + 1 for p in primes[a:b]))
    return Phi(x, a) + a - 1 - sum(pi[x // p] - pi[p] + 1 for p in primes[a:b])



main_(10**10)


t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')