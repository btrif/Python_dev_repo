#  Created by Bogdan Trif on 19-12-2018 , 10:28 AM.
# © o(^_^)o  Solved by Bogdan Trif  @   Completed on Sat, 5 Jan 2019, 16:38
#The  Euler Project  https://projecteuler.net
'''
                                    Sliding game      -       Problem 313

In a sliding game a counter may slide horizontally or vertically into an empty space.
The objective of the game is to move the red counter from the top left corner of a grid
to the bottom right corner; the space always starts in the bottom right corner.

For example, the following sequence of pictures show how the game can be completed in five moves on a 2 by 2 grid.

p313_sliding_game_1.gif

Let S(m,n) represent the minimum number of moves to complete the game on an m by n grid.

For example, it can be verified that S(5,4) = 25.

p313_sliding_game_2.gif

There are exactly 5482 grids for which S(m,n) = p2, where p < 100 is prime.

How many grids does S(m,n) = p^2, where p < 10^6 is prime?


'''
import time, zzz
# import gmpy2

class prime_generator() :
    def __init__(self, n):
        self.n = n
        self.P = self.prime_sieve()
        self.index = 0

    def prime_sieve(self):       # FOURTH      o(^_^)o
        sieve = [True] * self.n
        for i in range(3, int(self.n**0.5)+1, 2):
            if sieve[i]:
                sieve[ i*i :: 2*i ] = [False] * ( (self.n-i*i-1) // (2*i) +1 )
        # return [2] + [i for i in range(3, self.n , 2) if sieve[i] ]
        return [i for i in range(5, self.n , 2) if sieve[i] ]

    def next_prime(self):
        while self.index < len(self.P) :
            yield self.P[ self.index ]

            self.index += 1

###     Is square formula :
is_square = lambda x :  int( x**(1/2) )**2 == x

#   Triangular formula
T = lambda n : n*(n+1)//2

#   Inverse Triagular number formula :
nT = lambda T : pow(2*T+1/4, 1/2) - 1/2

print('\n--------------------------TESTS------------------------------')
t1  = time.time()

def slides(m, n) :
    S = m  + n - 2 - 3   #   Move only white space from bottom left to top right
    # print('only white moves = ', S )

    ####   RULES :      ####
    #   1.     For an horizontal move RED needs 4 white displacements, without the RED 1 move
    #   2.      For a diagonal movement RED needs 2 moves for the vertical displacement + another
    #            2 moves for the horizontal displacement, without the RED 2 own moves.
    #   3.      For the vertical move RED needs 4 white displacements, without the RED 1 own move
    ###   Convention: we will consider always m >= n ( cols >= rows )
    diag = (n-1) * ( 6 )
    S += diag
    # print('diag = ', diag, ' ;    S=', S )

    ### 2 CASES : m!=n & m==n
    if m != n :   horiz = (m-n-1)*5 + 3
    else : horiz = (m-n)*5

    S += horiz
    # print('horiz = ', horiz )

    # print('S= ', S)
    return S


slides(2, 2)

# @2018-12-19 --  I need to properly adjust this function. Work not completed ! FINISHED !!!

def problem_pattern_analysis(lim = 2000):
    cnt = 0

    for i in range(2, lim) :
        for j in range(2, i+1) :
            s =  slides(i, j )

            if is_square(s)  :
                p = int(gmpy2.sqrt(s))
                if gmpy2.is_prime(p) :
                    if p < 100 :
                        if i != j :  cnt +=2
                        else : cnt += 1
                        if i-j == 1 :



                            print(str(cnt) +'.     ',  i, j , '       i-j = ', i-j  ,   '       slides  = ',  s  , '     p = ', p ,'       i-p= ' , i-p ,'    nT(i-p) = ', nT(i-p)   )
    print('Answer : ', cnt)
    return cnt

# problem_pattern_analysis(2000)

# @2018-12-22, 12:40 : Now I must reverse Engineer the slides number. Based on the m,n columns & rows :
# find how choosing m &n will give as result the square of a prime
# What numbers do obey these properties ?
# So basically : find all m & n which will yield a result of sliders = 289 , where sqrt(289) = 17
# We observe that those combinations are  :
# 34.      38 37        i-j =  1        slides  =  289      sqare_root =  17
# 36.      39 34        i-j =  5        slides  =  289      sqare_root =  17
# 38.      40 31        i-j =  9        slides  =  289      sqare_root =  17
# 40.      41 28        i-j =  13        slides  =  289      sqare_root =  17
# 42.      42 25        i-j =  17        slides  =  289      sqare_root =  17
# 44.      43 22        i-j =  21        slides  =  289      sqare_root =  17
# 46.      44 19        i-j =  25        slides  =  289      sqare_root =  17
# 48.      45 16        i-j =  29        slides  =  289      sqare_root =  17
# 50.      46 13        i-j =  33        slides  =  289      sqare_root =  17
# 52.      47 10        i-j =  37        slides  =  289      sqare_root =  17
# 56.      48 7        i-j =  41        slides  =  289      sqare_root =  17
# 60.      49 4        i-j =  45        slides  =  289      sqare_root =  17
#
# Ooooh nice, I see some pattern now, but there are a few exceptions too !
# # @2018-12-22, 12:50  HAHA . Found it :
# 1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45,....for         i-j  difference.
# Now I must find only the starting number for i == m == nr of columns and problem is solved.

# @2019-01-05 - LAST OBSERVATION :
# Basically when i-j = 1 we obtain i-p to be triangular numbers with
# T_n = i-p = 0, 0, 1, 6, 10, 21, 28, 45, 78, 91, 136, 171, ...   These corespond to :
# n = 0, 0, 1, 3, 4, 6, 7, 9, 12, 13, 16, 18, 19, 21, 24, 27, 28
# Now the problem is solved because we must iterate over n's try to see if
# n*(n-1)/2 gives an i, j pair with i = j+1 which forms a difference slides = p^2
# and then we iterate up with i-j =1, 5, 9, 13, 17, ...etc... until we hit the limit j ==4.
# And this is the solution of this problem !
# 2.      3 2        i-j =  1        slides  =  9      p =  3        i-p=  0     nT(i-p) =  0.0
# 4.      5 4        i-j =  1        slides  =  25      p =  5        i-p=  0     nT(i-p) =  0.0
# 6.      8 7        i-j =  1        slides  =  49      p =  7        i-p=  1     nT(i-p) =  1.0
# 10.      17 16        i-j =  1        slides  =  121      p =  11        i-p=  6     nT(i-p) =  3.0
# 20.      23 22        i-j =  1        slides  =  169      p =  13        i-p=  10     nT(i-p) =  4.0
# 34.      38 37        i-j =  1        slides  =  289      p =  17        i-p=  21     nT(i-p) =  6.0
# 54.      47 46        i-j =  1        slides  =  361      p =  19        i-p=  28     nT(i-p) =  7.0
# 88.      68 67        i-j =  1        slides  =  529      p =  23        i-p=  45     nT(i-p) =  9.0
# 132.      107 106        i-j =  1        slides  =  841      p =  29        i-p=  78     nT(i-p) =  12.0
# 164.      122 121        i-j =  1        slides  =  961      p =  31        i-p=  91     nT(i-p) =  13.0
# 282.      173 172        i-j =  1        slides  =  1369      p =  37        i-p=  136     nT(i-p) =  16.0
# 362.      212 211        i-j =  1        slides  =  1681      p =  41        i-p=  171     nT(i-p) =  18.0
# 440.      233 232        i-j =  1        slides  =  1849      p =  43        i-p=  190     nT(i-p) =  19.0
# 622.      278 277        i-j =  1        slides  =  2209      p =  47        i-p=  231     nT(i-p) =  21.0
# 842.      353 352        i-j =  1        slides  =  2809      p =  53        i-p=  300     nT(i-p) =  24.0
# 1044.      437 436        i-j =  1        slides  =  3481      p =  59        i-p=  378     nT(i-p) =  27.0
# 1166.      467 466        i-j =  1        slides  =  3721      p =  61        i-p=  406     nT(i-p) =  28.0
# 1556.      563 562        i-j =  1        slides  =  4489      p =  67        i-p=  496     nT(i-p) =  31.0
# 1848.      632 631        i-j =  1        slides  =  5041      p =  71        i-p=  561     nT(i-p) =  33.0
# 1994.      668 667        i-j =  1        slides  =  5329      p =  73        i-p=  595     nT(i-p) =  34.0
# 2614.      782 781        i-j =  1        slides  =  6241      p =  79        i-p=  703     nT(i-p) =  37.0
# 3058.      863 862        i-j =  1        slides  =  6889      p =  83        i-p=  780     nT(i-p) =  39.0
# 3628.      992 991        i-j =  1        slides  =  7921      p =  89        i-p=  903     nT(i-p) =  42.0
# 4414.      1178 1177        i-j =  1        slides  =  9409      p =  97        i-p=  1081     nT(i-p) =  46.0
# 4812.      1277 1276        i-j =  1        slides  =  10201      p =  101        i-p=  1176     nT(i-p) =  48.0
# 5106.      1328 1327        i-j =  1        slides  =  10609      p =  103        i-p=  1225     nT(i-p) =  49.0
# 5738.      1433 1432        i-j =  1        slides  =  11449      p =  107        i-p=  1326     nT(i-p) =  51.0
# 6172.      1487 1486        i-j =  1        slides  =  11881      p =  109        i-p=  1378     nT(i-p) =  52.0
# 7226.      1598 1597        i-j =  1        slides  =  12769      p =  113        i-p=  1485     nT(i-p) =  54.0
# 10004.      2018 2017        i-j =  1        slides  =  16129      p =  127        i-p=  1891     nT(i-p) =  61.0
# 10486.      2147 2146        i-j =  1        slides  =  17161      p =  131        i-p=  2016     nT(i-p) =  63.0
# 11292.      2348 2347        i-j =  1        slides  =  18769      p =  137        i-p=  2211     nT(i-p) =  66.0
# 11708.      2417 2416        i-j =  1        slides  =  19321      p =  139        i-p=  2278     nT(i-p) =  67.0
# 14414.      2777 2776        i-j =  1        slides  =  22201      p =  149        i-p=  2628     nT(i-p) =  72.0
# 15016.      2852 2851        i-j =  1        slides  =  22801      p =  151        i-p=  2701     nT(i-p) =  73.0
# 16884.      3083 3082        i-j =  1        slides  =  24649      p =  157        i-p=  2926     nT(i-p) =  76.0
# 18694.      3323 3322        i-j =  1        slides  =  26569      p =  163        i-p=  3160     nT(i-p) =  79.0
# 20016.      3488 3487        i-j =  1        slides  =  27889      p =  167        i-p=  3321     nT(i-p) =  81.0
# 22484.      3743 3742        i-j =  1        slides  =  29929      p =  173        i-p=  3570     nT(i-p) =  84.0
# 24714.      4007 4006        i-j =  1        slides  =  32041      p =  179        i-p=  3828     nT(i-p) =  87.0
# 25616.      4097 4096        i-j =  1        slides  =  32761      p =  181        i-p=  3916     nT(i-p) =  88.0
# 30026.      4562 4561        i-j =  1        slides  =  36481      p =  191        i-p=  4371     nT(i-p) =  93.0
# 30970.      4658 4657        i-j =  1        slides  =  37249      p =  193        i-p=  4465     nT(i-p) =  94.0
# 32922.      4853 4852        i-j =  1        slides  =  38809      p =  197        i-p=  4656     nT(i-p) =  96.0
# 34112.      4952 4951        i-j =  1        slides  =  39601      p =  199        i-p=  4753     nT(i-p) =  97.0



t2  = time.time()
print('\n# Completed in :', round((t2-t1), 2 ), 's\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

def sliding_game( max_prime ) :

    P = prime_generator(max_prime)
    G = P.next_prime()
    Primes = P.prime_sieve()
    print('nr of primes = ', len ( Primes )  )

    count = 0
    index, j = 0, 0
    while index < len( Primes ) :
        p = next(G)     # we take for each prime step by step : 5, 7, 11, 13, 17, ....

        while True :
            t = T(j)        # triangular number  nT(i-p) = 0, 1, 6, 10, 21, 28, 45
            m = t+p
            n = m-1
            s = slides(m,n)
            if s == p*p :
                count += n//3

                if index % 10**3 == 0 :
                    print('i =', index , '     p = ', p , '      m =', m, '      n =' , n ,'     slides=' , s ,'    t= ', t, '    j= ', j , '    grids = ', n//3 )
                j+=1
                break
            else : j += 1

        index +=1

    print('\nNr of GRIDS      Answer =  ', (count+1)*2 )
    return (count+1)*2


sliding_game(10**6)         #   Nr of GRIDS      Answer =   2057774861813004        # Completed in : 1.65 s

t2  = time.time()
print('\n# Completed in :', round((t2-t1),2 ), 's\n\n')


### IDEAS from Euler forum      ###
'''
====    Sat, 6 Jul 2013, 09:01, EdM, France
Pour des raisons de symétrie, on peut supposer m >= n
On sépare m = n (on simple les réponses) et m > n (on double les réponses)

Lorsque m = n :
S(m, n) = 2*n - 2 + 3*[2*(n - 1) - 1] = 8*n - 11

Lorsque m > n :
S(m, n) = m + n - 2 + 5*(m - n - 1) + 3*[2*(n - 1)] = 6*m + 2*n - 13

PE313 : cpt = 2057774861813004 en 0.544 s
Appuyer sur ENTREE pour quitter le programme.


'''

print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()

# ====Wed, 8 Dec 2010, 23:09, quilan, USA
# Actually, while I don't know exactly how to apply the Meissel-Lehmer method yet,
# I've come up with a straight-forward way to use the old Lagrange method of PIE to solve for larger n.
#  This is also very slow, just only requires √n storage.
#
# Edit: Stepped through & figured out why Meissel's method works!
# Edit2: Lehmer up! Now things are positively zippy!
#
# I've adapted two approaches now, a depth-first recursive solution which is really short & intuitive code, ' \
#  'but is √n recursions deep. ' \
#  'The equivalent code was also unwrapped into a breadth-first solution which takes up slightly more memory, ' \
#  'but is much faster in Python. Explanation later.


def meissel_dfs(m,n):
    if(m<=1 or n<0): return m,m*(m+1)*(2*m+1)//6;

    a,b=meissel_dfs(m,n-1);
    c,d=meissel_dfs(m//primes[n],n-1);
    return a-c,b-primes[n]**2*d;

def meissel(m,on):

    q1={}; q2={}; q1[m]=q2[m]=1;
    for n in range(on,-1,-1):
        nq1={}; nq2={};
        for m in q1.keys(): nq1[m],nq2[m]=q1[m],q2[m];
        for m in q1.keys():
            if(m<primes[n]): continue;

            f1,f2=q1[m],q2[m];
            nm=m//primes[n];
            if(nm in nq1): nq1[nm]-=f1; nq2[nm]-=f2*primes[n]**2;
            else: nq1[nm],nq2[nm]=-f1,-f2*primes[n]**2;

        q1,q2=nq1,nq2; nq1={}; nq2={};

    t1=t2=0;
    for m in q1.keys(): f1,f2=q1[m],q2[m]; t1+=f1*m; t2+=f2*(m*(m+1)*(2*m+1)//6);
    return t1,t2;

#==================================================

db={};
def lehmer_meissel(m):
    global primes;
    if(m in db): return db[m];

    if(m < 1000):
        t1=t2=0;
        for p in primes:
            if(p>m): break;
            t1+=1;
            t2+=p**2;
        db[m]=t1,t2;
        return t1,t2;

    for n,p in enumerate(primes):
        if(p**3>m): break;

    t1,t2 = meissel(m,n);

    c,d=lehmer_meissel(primes[n]);
    t1+=c-1; t2+=d-1;
    for i in range(n+1,len(primes)):
        p=primes[i];
        if(p**2>m): break;
        a,b=lehmer_meissel(m//p);
        t1+=c-a; t2+=p**2*(d-b);
        c+=1; d+=p**2;

    db[m]=t1,t2;
    return t1,t2;

#==================================================

import pyprimes

def solve1(n):
    global primes;
    PB = pyprimes.primes_below(n)
    primes = [i for i in PB ]

    total=0;
    for sp,p in enumerate(primes):
        if(p**2>n): break;
        total+=p**2-1;

    print( "Calculating meissel(%d,%d)"%(n,sp))
    a,b=meissel(n,sp);
    total+=b-a;
    print( 2 + total//12)

def solve2(n):
    global primes;
    PB = pyprimes.primes_below(n)
    primes = [i for i in PB ]

    print( "Calculating lehmer_meissel(%d)"%(n))
    a,b=lehmer_meissel(n)
    print( 2 + (b-a)//12)


# solve1(10**6)
#
#
# solve2(10**6)


# Timings:
# n=10^6: 16 ms
# n=10^7: 78 ms, 1759498222925175334
# n=10^8: 484 ms, 1536134062912339617736
# n=10^9: 2.922 s, 1362687974541431583659762
# n=10^10: 32.985 s, 1224373805517995497732037766
# n=10^11: 212.551 s, 1111531720061055928931872721500
# n=10^12: 1386.324 s, 1017742330514805145619676589830416
# n=10^13: 10806.772 s, 938551482136725186389209468690305734
#
# New code runs in roughly O(n4/5).

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

'''
====    Fri, 18 Nov 2011, 09:33, Turing Machine ,  USA

First notice that due to symmetry, S(a,b) = S(b,a). 
Assume n = m. We will make moves alternating between right and down. 
To make the first red pawn move you need to make (m-1) + (n-1) slides. 
After that you need to make 3 slides to move the red pawn again until you are in the bottom right cell. 
WLOG, if the first move we made is right, there will be (m-1) down moves and (m-2) right moves.

S(m,m) = (m-1)+(m-1) + 3*((m-1) + (m-2)) = 8m - 11

WLOG let n > m. This means there are more columns than rows. 
The first move is again (m-1) + (n-1). 
Suppose we alternate between right and down moves like before, 
starting with a right move. Let us continue in this fashion until we are in the (m,m) cell, 
i.e. we hit the bottom row. 
The last move we made was down so the open cell is directly above the red pawn. 
This allows us to make an additional move to the right at a cost of 3 slides. 
Now the open cell is directly to the left of the red pawn, and the red pawn has (n-m-1) remaining cells to the right. 
In such a set up (open cell directly to the left) the minimum number of moves to move 
the red pawn once to the right is 5. 

S(m,n) = (m-1) + (n-1) + 3*((m-1) + (m-1)) + 5*(n-m-1) = 6n + 2m - 13

You should be able to convince yourself that this is the minimum number of slides required.

No square is = -11 = 5 (mod 8) so we do not need to worry about square grids. 
For all primes 3 <= p <= 10^6 we get (3n + m) = (p^2 + 13) / 2 = k. 
The number of combinations of m,n, n>m. n >m implies that n > k/4. 3*n + m = k implies that n < (k-2)/3.
 Since no square = -13 = 3 (mod 8), 4 will never divide k and n will never equal m.
'''



# S(m,m) = 8m - 11			but no square is ever = 5 (mod 8)
# S(m,n) = 2m + 6n - 13		n > m	so count it twice

if __name__ == "__main__":

    numgrids = 0

    p = [i for i in pyprimes.primes_below(10**6) ]
    for i in p[1:]:
        k = (i**2 + 13)//2
        numgrids += (k-2)//3 - k//4

    print(numgrids*2)


t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


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

