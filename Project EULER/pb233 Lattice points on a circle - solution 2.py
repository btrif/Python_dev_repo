#  Created by Bogdan Trif on 24-10-2017 , 9:24 PM.
# the number of lattice points on the circle is 420
# iff N factors into a product of primes not = 1 mod 4
# times p^a q^b r^c where (2a+1)(2b+1)(2c+1) = 105
# and p, q, r are congruent to 1 mod 4
#
# Possibilities:
#    p^3  q^2 r   7 * 5 * 3 = 105
#    p^7  q^3     15 * 7    = 105
#    p^10 q^2     21 * 5    = 105
#  <too large>    35 * 3    = 105
#
#  Let topNumber = 10^11 / (5^3 * 13^2).
#
#  Using a variant of the Eratosthenes sieve, we
#  produce a list of numbers k <= topNumber that have
#  no 1 mod 4 prime factors.
#
#  For all n <= topNumber we cache the sum of all
#  such k <= n. Then we iterate over each of the
#  three cases above and multiply by the cached
#  sum to conclude.


import math, time

import itertools

start_time = time.time()

def nice_solition():

  Lim = 10 ** 11
  K = 105
  Ans = 0

  def PrimeSieve(n):
    Primes, Primes1, Primes2 = [], [], []
    flag = [0] * (n + 1)
    for i in range(2, n + 1):
      if(flag[i] == 0):
        Primes.append(i)
        if(i % 4 == 1):
          Primes1.append(i)
        else:
          Primes2.append(i)
        for j in range(i * i, n + 1, i):
          flag[j] = 1
    return Primes, Primes1, Primes2

  Primes, Primes1, Primes2 = PrimeSieve(int(Lim / (5 * 5 * 5 * 13 * 13)))

  tempLim = int(Lim / (5 * 5 * 5 * 13 * 13 * 17))

  UnDivs = [0] + [i for i in range(1, tempLim + 1)]

  for p in Primes1:
    temp = p
    while(temp <= tempLim):
      UnDivs[temp] = 0
      temp += p

  for i in range(1, tempLim + 1):
    UnDivs[i] += UnDivs[i - 1]

  def Times(l):
    res = 1
    for k in l:
      res *= k
    return res

  def Power(list1, list2):
    assert len(list1) == len(list2)
    return [x ** y for x, y in zip(list1, list2)]

  def PrimeSigNums(l, k = 0, m = 1):
    res = 0
    if(len(l) == 0):
      res += m * UnDivs[int(Lim / m)]
      return res

    for i in range(k, len(Primes1)):
        j = Primes1[i:i + len(l)]
        if(len(l) != len(j)):
            break
        if(m * Times(Power(j, l)) > Lim):
            break
        res += PrimeSigNums(l[1:], i + 1, m * (Primes1[i] ** l[0]))
    return res

  def PrimeSigRec(n, arr = []):
    global Ans
    if(n == 1):
      Ans += PrimeSigNums(arr)
      return 0
    for i in range(1, n):
      if(n % (2 * i + 1) == 0):
        PrimeSigRec(n // (2 * i + 1), arr + [i])
    return 0

  PrimeSigRec(K)
  print(Ans)
  return Ans

print(" time: ", time.time() - start_time) # in seconds
# 271204031455541309  time:  18.151867



start_time = time.time()


def prime_sieve(n):       # FOURTH      o(^_^)o
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[ i*i :: 2*i ] = [False] * ( (n-i*i-1) // (2*i) +1 )
    return [2] + [i for i in range(3, n , 2) if sieve[i] ]


def solution2_lattice_points_on_circle(up_lim):
    up_lim = int(up_lim)
    min_comb = 5**3 * 13**2 #* 17
    max_prime = int( (up_lim)/min_comb )
    print('max prime = ', max_prime)
    primes = prime_sieve(max_prime)
    print('length primes = ', len(primes))

    primes_mod4_1 = [ i for i in primes if i%4==1  ]
    print('length P_mod4_is_1 = ' , len(primes_mod4_1) )
    # print ( primes_mod4_1[-50::]  )
    P4_1 = set(primes_mod4_1)

    # Building sieve for valid multipliers #
    lim = int(up_lim/(5**3 * 13**2 * 17) )+1
    print('non_mod4_1 primes lim = ', lim )
    sieve_non_mod4_1 = [ i for i in range(lim+1) ]

    for p in primes_mod4_1 :
        if p > lim : break
        # print(p)
        sieve_non_mod4_1[p :: p ] = [0] * ( lim//p  )

    print(sieve_non_mod4_1[:100])

    Sum = 0
    for i in range(0, len(primes_mod4_1)):
        p1 = primes_mod4_1[i]
        if p1**3 > up_lim : break
        for j in range(i+1,  len(primes_mod4_1)):
            p2 = primes_mod4_1[j]
            if p1**3* p2**2 > up_lim : break
            for k in range(j+1,  len(primes_mod4_1)):
                p3 = primes_mod4_1[k]
                if p1**3* p2**2 * p3 > up_lim : break

                # print(p1, p2, p3)
                perm = list(itertools.permutations([3,2,1]))
                for l in perm :
                    n = p1**l[0] * p2**l[1] * p3**l[2]
                    if n < up_lim :
                        rng = int(up_lim/n )+1
                        # print(p1, p2, p3 ,'      ',l, '     ', n ,'    rng = ', rng)
                        for o in range(1, rng) :
                            seeked = ( n*sieve_non_mod4_1[o])
                            # print('seeked nr =  ' , seeked, '       mult = ', o )
                            Sum += seeked

    ccnt = 0
    F = [ (7, 3 ) , ( 10, 2 )  ]
    for a in F :
        perm2 = list( itertools.permutations(a) )
        for l2 in perm2 :
            for i2 in range(0, len(primes_mod4_1)):
                p4 = primes_mod4_1[i2]
                if p4**10 > up_lim : break

                for j2 in range(i2+1,  len(primes_mod4_1)):
                    p5 = primes_mod4_1[j2]
                    n2 = p4**(l2[0]) * p5**(l2[1])

                    if n2 > up_lim : break
                    # print(p4, p5)

                    rng2 = int(up_lim/n2)+1
                    # print( p4, p5,'      ', l2 , '       ',n2 ,'      rng2 =  ', rng2, '     ' )

                    for o2 in range(1, rng2) :
                        seeked2 = ( n2*sieve_non_mod4_1[o2])
                        # print('seeked2 nr =  ' , seeked, '       mult2 = ', o2 )
                        Sum += seeked2


    # print('\nnrs diff = ', ccnt )
    print('\nTotal sum = ' , Sum )
    return Sum

solution2_lattice_points_on_circle(10**11)      #   Total sum =  271204031455541309     Completed in : 9.69  s


print(" time: ", time.time() - start_time) # in seconds
# 271204031455541309  time:  18.151867




