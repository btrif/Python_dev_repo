#  Created by Bogdan Trif on 20-09-2017 , 1:40 PM.

# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
                Triangles with non rational sides and integral area     -   Problem 390

Consider the triangle with sides √5, √65 and √68. It can be shown that this triangle has area 9.

S(n) is the sum of the areas of all triangles with sides √(1+b^2), √(1+c^2) and √(b^2+c^2) (for positive integers b and c )
that have an integral area not exceeding n.

The example triangle has b=2 and c=8.

S(10^6)=18018206.

Find S(10^10).


'''
import time, zzz
from math import sqrt

### Calculate Area using Heron Simplification - Archimedes Theorem
A = lambda x,y :  (1/2) * sqrt(x**2 * y**2 + x**2 + y**2)

# ##    Archimedes Area Calculation :
A_squared = lambda a, b : pow ( a*a + b*b +(a*b)**2, 1/2) / 2

print( ' Area for x,y =         ', A(2,8))

def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    from pyprimes import factorise
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]

# HELP from WOLFRAM
# http://www.wolframalpha.com/input/?i=simplify(+sqrt(++s*(s-+sqrt(1%2Bx%5E2))*(s-+sqrt(1%2By%5E2))*
# (s-+sqrt(x%5E2%2By%5E2))++)+,+s%3D(+sqrt(1%2Bx%5E2)%2Bsqrt(1%2By%5E2)%2Bsqrt(x%5E2%2By%5E2)+)%2F2++)


print('\n--------------------------TESTS------------------------------')
t1  = time.time()

def brute_force (lim, constraint) :     # @2019-01-04, 19:00 - Works well for the limit = 10^6
    cnt = 0
    Suma = 0
    for b in range(2, lim+1, 2) :
        # for c in range(3*b, 100*lim+1, 2) :
        for c in range(3*b, constraint * 2, 2) :
            Area = A(b,c)
            if Area > constraint : break
            if Area %1 == 0 and Area <= constraint :
                cnt+=1
                Suma += Area
                print(str(cnt)+'.     b =  ', b ,'    c =  ', c ,  '         Area = ' , Area ,'         c%b =', c%b , '       c/b = ', c/b  )

    print('\n Total Area = ', Suma)
    return Suma

# brute_force(10000, 10**10)





# ==== My APPROACH ===
# 1. First we must put in the Herons formula the values for √(1+b^2), √(1+c^2) and √(b^2+c^2)
#     It will result something like this :
# A = simplify( sqrt(  s*(s- sqrt(1+b^2))*(s- sqrt(1+c^2))*(s- sqrt(b^2+c^2))  ) , s=( sqrt(1+b^2)+sqrt(1+c^2)+sqrt(b^2+c^2) )/2  )
# A =  (1/2) * sqrt(b**2 * c**2 + b**2 + c**2)
#
# 2. Observe than only even numbers of b & c we have an integer Area .
# 3. Try to simplify more the problem

is_square = lambda x :  int(sqrt(x))**2 == x

def non_rational_sides_triangles(  constraint ) :
    cnt = 0
    Suma = 0
    for b in range(2 , int(sqrt(2*constraint))+1  ) :
        for c in range( b, constraint*10   ) :
            Q = ((b*b+1)*c*c + b*b )**(1/2)
            if Q > 2*constraint : break
            if Q%2 == 0 :
                A = int(Q/2)
                if A <= constraint :
                    cnt+=1
                    print(str(cnt)+'.     b =  ', b ,'    c =  ', c ,  '         Area = ' , A ) #, '    A_factors = ', get_factors(A)  , '        ',  get_factors(c) )
                    Suma += A

    print('\n Total Sum Area = ', Suma)
    return Suma

# non_rational_sides_triangles( 10**10)                           # WRONG Total Sum Area =  286926266212986
# @2017-09-22 - This problem takes too long ! can't find another method different than BRUTE FORCE !!!

# @2019-01-04 - The solution is I think to parametrize the equation :
# s^2 = b^2 + c^2 + b^2*c^2   in a similar fashion as pythagorean triplets are generated
# Maybe Brute force in JAVA ?

# 42861.     b =   49932     c =   393114          Area =  9814484126
# 42862.     b =   49946     c =   393224          Area =  9819982954
# 42863.     b =   49962     c =   393350          Area =  9826276352
# 42864.     b =   49972     c =   186498          Area =  4659839029
# 42865.     b =   49978     c =   393476          Area =  9832571766
# 42866.     b =   49980     c =   186528          Area =  4661334721
# 42867.     b =   49992     c =   393586          Area =  9838075658
# 42868.     b =   49994     c =   393602          Area =  9838869196

# def non_rational_sides_triangles1(  constraint ) :
#     # N = [i]
#     cnt = 0
#     Suma = 0
#     for b in range(2, int(sqrt(constraint))//2 , 2) :
#         step = b*b +1
#         for i in range( 3*b, int(constraint)*2 , 2 ) :
#             n = (i*i-b*b) / step
#             # print('i = ' , i ,  ' b=' , b, ', n =  ',  n,  '    c=' , sqrt(n) , '     step =  ', step)
#             if is_square(n)   :
#                 c = sqrt(n)
#                 Q = ((b*b+1)*n + b*b )**(1/2)
#                 if Q%2 == 0 :
#                     A = int(Q/2)
#                 # if A <= constraint :
#                     cnt+=1
#                     print(str(cnt)+'.     b =  ', b ,'    c =  ', c ,  '         Area = ' , A ) #, '    A_factors = ', get_factors(A)  , '        ',  get_factors(c) )
#                     Suma += A
#
#     return print('\n Total Sum Area = ', Suma)

# non_rational_sides_triangles1( 10**6)

t2  = time.time()
print('\nCompleted in :', round((t2-t1),2), 's\n\n')

print('\n================  My FIRST SOLUTION,  1 hour  ===============\n')
t1  = time.time()


def second_solution (limit) :
    N = int(limit * 2)
    S, count = 0, 0
    b = 2
    while  b*b <= N :
        upper_bound = N // (b * b )
        for t in range(2, upper_bound+1, 2 ) :
            if (t % 1e8 == 0) :
                print("t = ", t,  '    upper_bound =  ' ,upper_bound);
            s = b * b * t * t - b * b + t * t
            v = sqrt(s)
            if v %1 == 0 :
                c = b * t + v
                Area = b * c + t
                if Area > N : break

                count += 1
                print(str(count) + '.       b = ', b , '      c= ', c   ,'    Area = ', Area//2 ,'       t= ' , t )
                S += Area / 2

        b+=2

    print('\n Answer = ', S )
    return S

second_solution(10**6)              # It verifies for 10**6, gives the correct answer !

# WRONG  : Answer =  6209341318032.0               #               Completed in : 3822.25962 s


# @2019-01-27, 20:49:     I must understand the problem and parametrize it properly.

t2  = time.time()
print('\nCompleted in :', round((t2-t1)/60,2), 'mins\n\n')


'''
Rosephu C++
#include <cstdio>
#include <cmath>
using namespace std;

const long long N = 1e10 * 2;

int main() {
  long long ans = 0;
  for (long long a = 2; a * a + 1 <= N; a += 2) {
    long long upper_bound = N / (a * a + 1);
    for (long long t = 2; t <= upper_bound; t += 2) {
      if (t % 10000000 == 0)
        printf("%lld %lld\n", t, upper_bound);
      long long s = a * a * t * t - a * a + t * t;
      long long v = sqrt(s);
      if (v * v == s) {
        long long b = a * t + v;
        long long n = a * b + t;
        if (n > N)
          break;
        ans += n / 2;
        // printf("%lld %lld %lld\n", a, b, n);
      }
    }
  }
  printf("%lld\n", ans);
  return 0;
}
'''




# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 5,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 6,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 7,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 8,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 9,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 10,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 11,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 12,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')




