#  Created by Bogdan Trif on 25-03-2018 , 11:02 PM.
# © o(^_^)o  Solved by Bogdan Trif  @   Completed on Mon, 14 May 2018, 16:30
#The  Euler Project  https://projecteuler.net
'''
        Triangles with integral sides and an integral angle         -           Problem 279

How many triangles are there with integral sides, at least one integral angle (measured in degrees),
and a perimeter that does not exceed 10^8  ?

'''
import time, zzz
from math import sin, cos, asin, acos, sqrt, pi, gcd

def gcd3(x, y, z):
    return gcd(gcd(x, y), z)


def triangle_primitive_triplets_60_gen(  ) :      # o(^_^)o #  Made by Bogdan Trif @ 2017-02-21, 16:10
    ##### 60 degree TRIANGLES GENERATOR
    # http://www.geocities.ws/fredlb37/node9.html
    ''':Description: GENERATOR for Triangle primitive triplets of 60 degrees
    :param up_lim: integer, the limit to which the sum of sides a,b,c is up to
    :return: the sides of the 60 degree triangle , p ,q, r   '''
    from math import gcd
    cnt=0
    m, n = 1, 1
    while True :   # If needed we can set a limit based on m**2-n**2
        for n in range(1, m) :      ### range(1,m) as we need only p > 0 !!!!!!!!
            if gcd(m,n)==1 : #and (m-n)%3 !=0  :         #!!!! if we omit the %3 condition we will get duplicates !!!
                a = 2*m*n + m**2
                b = 2*m*n + n**2
                c = m**2+n**2+m*n
                cnt+=1
                # print(str(cnt)+'.         '  , a, b, c ,'       sum =',  a+b+c ,'            m,n =',m, n)
                g = gcd3(a, b, c)
                yield a//g, b//g, c//g
        m+=1


TPT60 = triangle_primitive_triplets_60_gen(  )
# TPT61 = triangle_primitive_triplets_60_gen1(  )
# TPT62 = triangle_primitive_triplets_60_gen2(  )

for i in range(10**2):
    f = next(TPT60)
    # if f[1] in[297, 333, 360 ] :
    print(' f =  ', f  )



def triangle_primitive_triplets_120_gen(  ) :      # o(^_^)o #  Made by Bogdan Trif @ 2017-02-19, 13:10
    ##### 120 degree TRIANGLES GENERATOR
    # http://www.geocities.ws/fredlb37/node9.html
    ''':Description: GENERATOR for Triangle primitive triplets of 120 degrees
    :param up_lim: integer, the limit to which the sum of sides a,b,c is up to
    :return: the sides of the 120 degree triangle , p ,q, r   '''
    from math import gcd
    # cnt=0
    m, n = 1, 1
    while True :   # If needed we can set a limit based on m**2-n**2
        for n in range(1, m) :      ### range(1,m) as we need only p > 0 !!!!!!!!
            if gcd(m,n)==1 and (m-n)%3 !=0  :         #!!!! if we omit the %3 condition we will get duplicates !!!
                p = (m**2-n**2)
                q = (2*m*n+n**2)
                r = (m**2+n**2+m*n)
                if p > 0 :
                    # cnt+=1
                    # print(str(cnt)+'.         '  , p, q, r ,'       sum =',  p+q+r ,'            m,n =',m, n)#, compute_triangle_angles( [ p, q, r ] )  )
                    yield p,q, r
        m+=1

# TPT = triangle_primitive_triplets_120_gen(  )
# for i in range(40):
#     print(next(TPT))


def Pythagorean_primitive_triplets_gen():    # by Bogdan Trif @ 2017-01-21, 16:30     ### ( ͡° ͜ʖ ͡°)  FASTEST  ( ͡° ͜ʖ ͡°)  ###
    ''':Usage:      >>> pyt = Pythagorean_primitive_triplets_gen()
                        # >>> next(pyt)
                        # >>> for i in Pythagorean_primitive_triplets_gen(): print(i)
    :param i:   i
    :param j:   j
    :return:    a,b,c - primitive pythagorean triplet
    '''
    m = 1
    while True :
        for n in range(1, m):           ### range(1,m) as we need only a > 0 !!!!!!!!
            a = m**2-n**2
            b = 2*m*n
            c = m**2 + n**2
            if gcd(a,b) ==1 :           #   Assure that we generate ONLY primitive Pythagorean triplets
                print(' m, n = \t',m, n,'            a,b,c =\t',sorted((a,b,c)))
                # yield a,b,c
        m+=1

# PT = Pythagorean_primitive_triplets_gen()
# cnt=0
# for i in range(40) :
#     cnt+=1
#     print(str(cnt)+'.     ',next(PT))


# https://pdfs.semanticscholar.org/b1ed/c10b2aa179abfc179690136705b6e6324d1a.pdf
# http://www.mathwarehouse.com/triangle-calculator/online.php


print('\n--------------------------TESTS & BRUTE FORCE ------------------------------')
t1  = time.time()


def get_idea_and_proof_of_concept( perim ) :        # Correct Brute Force
    eps = 1e-9
    cnt = 0
    for a in range( 1, perim//3 +1 )  :
        for b in range( a, perim//2 +1) :
            for c in range( b, a+b ) :
                if a+b +c > perim : break
                A = ( acos ( (b**2 + c**2 - a**2) / (2*b*c) ) ) *180/pi
                B = ( acos ( (c**2 + a**2 - b**2) / (2*c*a) ) ) *180/pi
                C = 180-A-B
                if abs(round(A) - A) <eps or abs(round(B) - B) <eps or abs(round(C) - C) <eps  :
                    if round(A) ==60 or round(B) ==60 or round(C) == 60 :
                        cnt +=1
                        if a != b   :
                            print(str(cnt)+'.     ', 'a , b, c = ', a, b, c , '       angles A, B, C =  ', A, B, C)
    return print('\nBRUTE FORCE Total cnt : ', cnt)


# get_idea_and_proof_of_concept(10**3)     # Generate all triangles with 60, 90, 120 & equilateral triangles





t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n================  My FIRST SOLUTION,  O(n) ,  >1 hour , Can be improved ===============\n')
t1  = time.time()

def triangles_with_integral_sides(lim) :

    m = 1
    cnt = lim//3
    print('init cnt = ', cnt)
    while m*m <= lim *4 :
        print('m = ', m)
        for n in range(1, m):           ### range(1,m) as we need only a > 0 !!!!!!!!
            # print('m, n = ', m, n )
            if m*n > 3.5 * lim : break
            if ( 2*m**2 + 2*m*n ) <=  lim :
                # print('m, n =  ', m, n)

                ## Pythagorean_primitive_triplets_gen 90
                a = m**2-n**2
                b = 2*m*n
                c = m**2 + n**2
                if gcd(a,b) ==1 :           #   Assure that we generate ONLY primitive Pythagorean triplets
                    # print(' m, n = \t',m, n,'            a,b,c =\t',sorted((a,b,c)))
                    if a+b+c <= lim :
                        cnt += lim//(a+b+c)
                        # print(str(cnt)+'.      ' ,a,b,c ,'     90 deg : ', lim//(a+b+c) )

            # triangle_primitive_triplets_60_gen
            # if ( 2*m**2 + 5*m*n + 2*n**2 ) <= 3*lim :
            # if m%3 == n%3: continue

            if gcd(m,n)==1 : #and (m-n)%3 !=0  :         #!!!! if we omit the %3 condition we will get duplicates !!!

                u = 2*m*n + m**2
                v = 2*m*n + n**2
                w = m**2 + n**2 + m*n

                g = gcd3(u, v, w)
                u_, v_, w_ = sorted([u//g, v//g, w//g])
                if u_+ v_+ w_ <= lim :
                    cnt += lim//(u_+ v_+ w_)
                    # print( str(cnt)+'.      ' , u_, v_, w_   ,'     60 deg : ', lim//(u_+ v_+ w_) )

                    # triangle_primitive_triplets_120_gen
            # if ( 2*m**2 + 3*m*n + n**2 ) <= 3*lim :
            if gcd(m,n)==1 :
                if (m-n)%3 !=0  :         #!!!! if we omit the %3 condition we will get duplicates !!!
                    p = (m**2 - n**2)
                    q = (2*m*n + n**2)
                    r = (m**2 + n**2 + m*n)
                    if p+q+r <= lim  :
                        cnt += lim//(p+ q+ r )

                        # print( str(cnt)+'.      ' ,  p,q, r ,'     120 deg : ', lim//(p+ q+ r ) )

        m+=1

    return print('\nANSWER : ', cnt )

triangles_with_integral_sides(10**6)
# triangles_with_integral_sides(10**8)        # ANSWER :  416577688



t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')        # Completed in : 4250080.09 ms


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  O(N^2/3) Algorithm  --------------------------')
t1  = time.time()

# === Fri, 25 Mar 2016, 14:44, Min_25, Japan

from math import sqrt
from itertools import count

def isqrt(n, dblcutoff=1<<52):
  if n < dblcutoff:
    return int(sqrt(n))
  x = int(sqrt(n * (1 + 1e-14)))
  while True:
    y = (x + n // x) >> 1
    if y >= x:
      return x
    x = y

def icbrt(n):
  if n <= 0:
    return 0

  x = int(n ** (1. / 3.) * (1 + 1e-12))
  while True:
    y = (2 * x + n // (x * x)) // 3
    if y >= x:
      return x
    x = y

def accumulated(seq):
  ret = seq[:]
  for i in range(1, len(seq)):
    ret[i] += ret[i - 1]
  return ret

def moebius_sieve(N):
  ret = [i for i in range(N + 1)]
  for p in range(2, N + 1):
    if ret[p] != p:
      continue
    for j in range(p * p, N + 1, p * p):
      ret[j] = 0
    for j in range(p, N + 1, p):
      if ret[j] > 0:
        ret[j] = -1
      elif ret[j] < 0:
        ret[j] = 1
  return ret

def C(N, ac, c1, c2, de):
  c0 = 2 * N * de
  ret = 0
  for x in range(1, isqrt(N // ac) + 1):
    ret += (isqrt(c0 + c1 * x ** 2) - c2 * x) // de
  return ret

def H(N, a, b, c, d):
  """
  Return the \sum _{x=1} _{y=1} \frac{N}{(a*x+b*y)*(c*x+d*y)}

  Assume that a, b, c, d >= 1.
  """
  if b * d < a * c:
    a, b, c, d = b, a, d, c
  ac = a * c
  c1 = (a * d - b * c) ** 2
  c2 = (a * d + b * c)
  de = 2 * b * d

  cbrt_N = int(N ** 0.30)

  ret = 0
  for i in range(1, cbrt_N):
    ret += C(N // i, ac, c1, c2, de)
  ret -= (cbrt_N - 1) * C(N // cbrt_N, ac, c1, c2, de)

  for x in count(1):
    ax = a * x
    cx = c * x
    if N < cbrt_N * (ax + b) * (cx + d):
      break
    for y in count(1):
      de = (ax + b * y) * (cx + d * y)
      t = N // de
      if t < cbrt_N:
        break
      ret += t
  return ret

def prob279(N=10**8):
  """
  10 **  8: 416577688, 0.217 sec.
  10 **  9: 4721065834, 0.875 sec.
  10 ** 10: 52763559619, 3.836 sec.
  10 ** 11: 583164702017, 17.187 sec.
  10 ** 12: 6386938152502, 83.013 sec.
  10 ** 13: 69422292916726, 365.179 sec.
  10 ** 14: 749752043588357, 1736.224 sec.
  """
  def S(N, a, b, c, d):
    v = icbrt(N)
    ret = 0
    prev = isqrt(N)
    for i in range(1, v + 1):
      curr = isqrt(N // (i + 1))
      ret += (mertens[prev] - mertens[curr]) * H(i, a, b, c, d)
      prev = curr
    for i in range(1, prev + 1):
      if mu[i]:
        ret += mu[i] * H(N // i ** 2, a, b, c, d)
    return ret

  mu = moebius_sieve(isqrt(N))
  mertens = accumulated(mu)
  ans = 0

  M = N // 2
  while M:
    ans += S(M, 1, 1, 1, 2)
    ans -= S(M, 2, 1, 2, 2)
    M //= 4

  M = N
  while M:
    ans += S(M, 2, 3, 1, 2)
    ans -= S(M, 6, 3, 3, 2)
    M //= 9

  M = N
  while M:
    ans += S(M, 2, 3, 1, 3)
    ans -= S(M, 6, 3, 3, 3)
    M //= 9

  M = N // 3
  while M:
    ans += S(M, 1, 2, 1, 1)
    ans -= S(M, 3, 2, 3, 1)
    M //= 9

  ans += N // 3
  print(ans)

# prob279(10 ** 8)

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 2, O(N^1/3) Algorithm  --------------------------')
t1  = time.time()

# ==== Fri, 25 Mar 2016, 14:44, Min_25
# It seems that we can compute C(N,a,b,c,d) in O(N1/3) time using the convex hull technique
# suggested by Lucy_Hedgehog and Animus in Problem 540.
# For example, we can get C(1024,2,1,1,1)=346573590279119101559484 in about 28 seconds !
#
# So, theoretically, we can compute the answer in O(N3/5) by choosing v=⌊N2/5⌋.

from math import sqrt
from itertools import count

def isqrt(n, dblcutoff=1<<52):
  if n < dblcutoff:
    return int(sqrt(n))
  x = int(sqrt(n * (1 + 1e-14)))
  while True:
    y = (x + n // x) >> 1
    if y >= x:
      return x
    x = y

def icbrt(n):
  if n <= 0:
    return 0

  x = int(n ** (1. / 3.) * (1 + 1e-12))
  while True:
    y = (2 * x + n // (x * x)) // 3
    if y >= x:
      return x
    x = y

def accumulated(seq):
  ret = seq[:]
  for i in range(1, len(seq)):
    ret[i] += ret[i - 1]
  return ret

def moebius_sieve(N):
  ret = [i for i in range(N + 1)]
  for p in range(2, N + 1):
    if ret[p] != p:
      continue
    for j in range(p * p, N + 1, p * p):
      ret[j] = 0
    for j in range(p, N + 1, p):
      if ret[j] > 0:
        ret[j] = -1
      elif ret[j] < 0:
        ret[j] = 1
  return ret

def C(N, ac, c1, c2, de):
  c0 = 2 * N * de
  ret = 0
  for x in range(1, isqrt(N // ac) + 1):
    ret += (isqrt(c0 + c1 * x ** 2) - c2 * x) // de
  return ret

def sum_abc(a, b, c, r):
  if r <= 0:
    return 0

  if a == 0:
    return (b // c) * r

  ret = 0
  if not (0 <= a < c):
    q, a = divmod(a, c)
    return q * (r * (r + 1) // 2) + sum_abc(a, b, c, r)

  if not (0 <= b < c):
    q, b = divmod(b, c)
    return q * r + sum_abc(a, b, c, r)

  q = (a * r + b) // c
  return r * q - sum_abc(c, -b - 1, a, q)

def fast_C(N, a, b, c, d):
  if a == c and b == d:
    r = isqrt(N)
    return sum_abc(-a, r, b, r // a)

  if a * c < b * d:
    a, b, c, d = b, a, d, c
  ac2, bd2, sp, sm = 2 * a * c, 2 * b * d, a * d + b * c, a * d - b * c
  c0 = 2 * N * bd2

  f = lambda x: (isqrt(c0 + (sm * x) ** 2) - sp * x) // bd2
  inside = lambda x, y: (a * x + b * y) * (c * x + d * y) > N
  outside = lambda x, y, dx, dy: dy * (bd2 * y + sp * x) >= dx * (ac2 * x + sp * y)

  end = isqrt(N // (a * c)) + 1
  if end <= 3:
    return sum(f(x) for x in range(1, end))

  x = 0
  y = int(f(x) + 1)
  stack = [(1, 0), (0, 1)]

  ret = 0
  while 1:
    ldx, ldy = stack.pop()
    while inside(x + ldx, y - ldy):
      if y <= ldy:
        break
      x, y = x + ldx, y - ldy
      ret += ldx * (y - 1) + ((ldx - 1) * (ldy + 1) >> 1)

    if y <= ldy:
      for x2 in range(x + 1, end):
        ret += f(x2)
      break

    udx, udy = ldx, ldy
    while 1:
      ldx, ldy = stack[-1]
      if inside(x + ldx, y - ldy):
        break
      udx, udy = ldx, ldy
      stack.pop()

    while 1:
      mdx, mdy = ldx + udx, ldy + udy
      if inside(x + mdx, y - mdy):
        ldx, ldy = mdx, mdy
        stack += [(ldx, ldy)]
      else:
        if outside(x + mdx, y - mdy, ldx, ldy):
          break
        udx, udy = mdx, mdy
  return ret

def H(N, a, b, c, d):
  """
  Return the \sum _{x=1} _{y=1} \frac{N}{(a*x+b*y)*(c*x+d*y)}

  Assume that a, b, c, d >= 1.
  """
  if b * d < a * c:
    a, b, c, d = b, a, d, c
  ac = a * c
  c1 = (a * d - b * c) ** 2
  c2 = (a * d + b * c)
  de = 2 * b * d

  v = int(max(1, (N // ac) ** 0.355))
  ret = 0
  for i in range(1, v):
    M = N // i
    if M > 2500:
      ret += fast_C(M, a, b, c, d)
    else:
      ret += C(M, ac, c1, c2, de)
  if v > 1:
    ret -= (v - 1) * fast_C(N // v, a, b, c, d)

  for x in count(1):
    ax = a * x
    cx = c * x
    if N < v * (ax + b) * (cx + d):
      break
    for y in count(1):
      de = (ax + b * y) * (cx + d * y)
      t = N // de
      if t < v:
        break
      ret += t
  return ret

def prob279(N=10**8):
  """
  10 **  8: 416577688, 0.217 sec.
  10 **  9: 4721065834, 0.628 sec.
  10 ** 10: 52763559619, 2.277 sec.
  10 ** 11: 583164702017, 7.691 sec.
  10 ** 12: 6386938152502, 26.606 sec.
  10 ** 13: 69422292916726, 107.763 sec.
  10 ** 14: 749752043588357, 397.397 sec.
  10 ** 15: 8052811580984275, 1553.017 sec.
  10 ** 16: 86081027259750675, 6167.645 sec.
  """
  def S(N, a, b, c, d):
    v = icbrt(N)
    ret = 0
    prev = isqrt(N)
    for i in range(1, v + 1):
      curr = isqrt(N // (i + 1))
      ret += (mertens[prev] - mertens[curr]) * H(i, a, b, c, d)
      prev = curr
    for i in range(1, prev + 1):
      if mu[i]:
        ret += mu[i] * H(N // i ** 2, a, b, c, d)
    return ret

  mu = moebius_sieve(isqrt(N))
  mertens = accumulated(mu)
  ans = 0

  M = N // 2
  while M:
    ans += S(M, 1, 1, 1, 2)
    ans -= S(M, 2, 1, 2, 2)
    M //= 4

  M = N
  while M:
    ans += S(M, 2, 3, 1, 2)
    ans -= S(M, 6, 3, 3, 2)
    M //= 9

  M = N
  while M:
    ans += S(M, 2, 3, 1, 3)
    ans -= S(M, 6, 3, 3, 3)
    M //= 9

  M = N // 3
  while M:
    ans += S(M, 1, 2, 1, 1)
    ans -= S(M, 3, 2, 3, 1)
    M //= 9

  ans += N // 3
  print(ans)

prob279(10 ** 6)

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

#
# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 5,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 6,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 7,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 8,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 9,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 10,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 11,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 12,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')




