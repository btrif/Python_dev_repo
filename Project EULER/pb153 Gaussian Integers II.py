#  Created by Bogdan Trif on 23-10-2017 , 7:07 PM.


from math import sqrt
import time


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

def prob153(N=10**8):
  """
  10 **  9: 1797231035470229962, 0.586 sec.
  10 ** 10: 179726445633260218662, 2.140 sec.
  10 ** 11: 17972750272542089793485, 9.971 sec.
  10 ** 12: 1797278370292056629263518, 47.969 sec.
  10 ** 13: 179727942749349269842849984, 256.118 sec.
  """
  def S(n):
    v = isqrt(n)
    ret = 0
    for i in range(v, 0, -1):
      t = n // i
      ret += t * (2 * i + t + 1)
    ret -= v * v * (v + 1)
    return ret >> 1

  def C(n):
    v = isqrt(n)
    w = isqrt(n // 2)
    ret = 0
    for i in range(v, w, -1):
      t = isqrt(n - i * i)
      ret += t * (2 * i + t + 1)
    ret += w * w * (w + 1)
    return ret >> 1

  def sum_imaginary_numbers(N):
    def T(n):
      return n * (n + 1) // 2

    def calc_coprime(n):
      ret = smalls[n] if n < w else larges[N // n]
      u = icbrt(n)
      prev = T(isqrt(n))
      for i in range(1, u + 1):
        curr = T(isqrt(n // (i + 1)))
        ret -= (prev - curr) * smalls[i]
        prev = curr
      for i in range(2, isqrt(n // (u + 1)) + 1):
        d = n // (i * i)
        ret -= i * (smalls[d] if d < w else larges[N // d])
      return ret

    v = isqrt(N)
    w = N // v

    larges = [0] + [C(N // i) for i in range(1, v + 1)]
    smalls = [0] + [C(i) for i in range(1, w)]

    for i in range(1, w):
      smalls[i] = calc_coprime(i)

    for i in range(v, 0, -1):
      larges[i] = calc_coprime(N // i)

    for i in range(1, v):
      larges[i] -= larges[i + 1]
    larges[v] -= smalls[w - 1]
    for i in range(w - 2, 0, -1):
      smalls[i+1] -= smalls[i]

    ret = 0
    for i in range(1, w):
      if smalls[i] > 0:
        ret += smalls[i] * S(N // i)
    for i in range(1, v + 1):
      ret += larges[i] * S(i)
    return 2 * ret

  ans = sum_imaginary_numbers(N) + S(N)
  return ans

t1  = time.time()

print(prob153(10 ** 9))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


