#  Created by Bogdan Trif on 24-10-2017 , 10:44 PM.

def prime_sieve(n):       # FOURTH      o(^_^)o
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[ i*i :: 2*i ] = [False] * ( (n-i*i-1) // (2*i) +1 )
    return [i for i in range(3, n , 2) if sieve[i] ]


# print( prime_sieve(30) )


def prime_sieve_2(n):       # FOURTH      o(^_^)o
    sieve = [True] * n
    for i in range(2, int(n**0.5)+1, 1):
        if sieve[i]:
            sieve[ i*i :: i ] = [False] * ( (n-i*i-1) // (i) +1 )
            print(i, n,  i*i,    ( n-i*i-1) , i , ( (n-i*i-1) // (i)  ),  '    ( (n-i*i-1) // (i) +1 ) =', ( (n-i*i-1) // (i) +1 )    )
    return [i for i in range(2, n , 1) if sieve[i] ]


lim = 100
P = prime_sieve_2(100)
print( P )


mod4_1 = [ i for i in P if i%4==1 ]
print(mod4_1)

# Builds a sieve with numbers which are NOT  =1 (mod 4) !!!!!!
def sieve_non_mod4_1(lim) :
    sieve = [i for i in range(lim+1)]
    print(sieve)
    for p in mod4_1 :
        print(p)
        sieve[p :: p ] = [0] * ( lim//p  )

    print(sieve)
sieve_non_mod4_1(lim)