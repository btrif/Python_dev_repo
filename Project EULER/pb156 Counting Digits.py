#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
                               Counting Digits      -       Problem 156
Starting from zero the natural numbers are written down in base 10 like this:
0 1 2 3 4 5 6 7 8 9 10 11 12....

Consider the digit d=1. After we write down each number n, we will update the number of ones that have occurred
and call this number f(n,1). The first values for f(n,1), then, are as follows:

                                                            n	f(n,1)
                                                            0	0
                                                            1	1
                                                            2	1
                                                            3	1
                                                            4	1
                                                            5	1
                                                            6	1
                                                            7	1
                                                            8	1
                                                            9	1
                                                            10	2
                                                            11	4
                                                            12	5
Note that f(n,1) never equals 3.
So the first two solutions of the equation f(n,1)=n are n=0 and n=1. The next solution is n=199981.

In the same manner the function f(n,d) gives the total number of digits d that have been written down
after the number n has been written.
In fact, for every digit d ≠ 0, 0 is the first solution of the equation f(n,d)=n.

Let s(d) be the sum of all the solutions for which f(n,d)=n.
You are given that s(1)= 22.786.974.071.

Find ∑ s(d) for 1 ≤ d ≤ 9.

Note: if, for some n, f(n,d)=n for more than one value of d this value of n is counted again
for every value of d for which f(n,d)=n.
'''

import time, zzz

D = {(k+1): int((k+1)*10**k) for k in range(-1, 25 )}

def f(n, d, D ) :
    ''' :Description: function which counts the number of appearances of a digit d
    to a number n. It uses an external dictionary as a memo to be faster.
    :param n: int, number to test
    :param d: digit which is tested
    :param D: the dictionary, external
    :return: number of digits d of that number    '''
    # Dictionary will be EXTERNAL
    L = [ int(i) for i in str(n) ]
    # D = {(k+1): int((k+1)*10**k) for k in range(-1, len(L))}
    # STEP 1 : FIRST decompose the number into powers of base 10 :
    digits = 0
    for j in range(len(L)) :
        w = len(str(n))-j-1
        diff = L[j] - d
        if L[j] == d :
            digits += n%10**(len(L)-j-1) +1
#             print(j, d, n%10**(len(L)-j-1))
        if diff > 0 :  digits += 10**(w)
        # print(' diff : ', L[j]  ,diff, 'digits : ' ,10**(w), ' dict=',D[w] , '  w=',w)
        digits += L[j] * D[w]

    return digits

print( 'f function test: \t' , f(9006, 6, D) )

def monotonic(L) :
    ''':Scope:   Function which checks the last three elements in a list for monotony.
    If the elements are monotonic return True,
    If the elements are NON-monotonic return False'''
    a, b, c = L[-3::]
    if a<=b <=c or a>=b >=c : return True
    return False

def find_elem(Diff):
    '''Returns the position of the non-monotonic element and the previous one'''
    for i in range(len(Diff)-2) :
        I = Diff[i:i+3]
        a, b, c = I
        # print( I)
        if  (a < b > c) == True or (a > b < c)== True :
            return i,i+1

    return None

def binary_search(low, high, digit) :
    g_low, g_high =  f(low, digit ,D), f(high, digit ,D)
    ldiff, hdiff = low-g_low, high-g_high
    # print('low, high = ', low, high , '   g_low, g_high =',g_low, g_high , '   ldiff,  hdiff = ', ldiff, hdiff )

    if abs(ldiff)< 10 :
        return low-30 ;
    if abs(hdiff)< 10 :
        return high-30 ;

    while ( abs(ldiff) > 5 and abs(hdiff) > 5 ) and  ( abs(hdiff-ldiff) > 5 ) :
        # print('ldiff, hdiff ,  abs diff : ', ldiff, hdiff ,'  ',abs(hdiff-ldiff) )
        if abs(ldiff) >= abs(hdiff) :
            low = (low+high)//2

#             if ldiff >0 and  hdiff > 0 :# we shift position back
#                 high_tmp = 2*high-low
#                 low, high = high, high_tmp

#             else :
#                 low = (low+high)//2
            g_low, g_high =  f(low, digit ,D), f(high, digit ,D)
            ldiff, hdiff = low-g_low, high-g_high
            # print('C1 :     low, high = ' ,low, high , '; ldiff = ',ldiff, ';  hdiff =', hdiff,'  ->' , g_low, g_high  )


        elif abs(ldiff) < abs(hdiff) :
#             if (abs(ldiff) < 10 or abs(hdiff) < 10) : return low-15
            if ( ldiff >= 0 and hdiff <= 0) or ( ldiff <= 0 and hdiff >= 0) :
                low = (low+high)//2
            if ( ldiff >= 0 and hdiff >= 0) :    #shift right
                high = (low+high)//2
            if ( ldiff <= 0 and hdiff <= 0) :      #shift left
                low_tmp = abs(high-low)
                low, high = abs(low - low_tmp) , high - low_tmp


            g_low, g_high =  f(low, digit ,D), f(high, digit ,D)
            ldiff, hdiff = low-g_low, high-g_high
            # print('C2 :     low, high = ' ,low, high , '; ldiff = ',ldiff, ';  hdiff =', hdiff,'  ->' ,g_low, g_high  )

            if (abs(ldiff) < 10 or abs(hdiff) < 10) : return abs(low-15)


    return False


# binary_search(100003, 280010, 1)

print('--------------------------TESTS------------------------------')
t1  = time.time()


def string_brute_force_check(up, d):
    cnt = 0
    for n in range(1, up+1):
        cnt += str(n).count(str(d))
    # print(len(s))
    # print( s.count(str(d))  )
        if n == cnt :
            print(n)
    return cnt

# string_brute_force_check(10**7, 1)

print('string_brute_force_check : \t ',string_brute_force_check(15, 1) )
print('string_brute_force_check : \t ',string_brute_force_check(199981, 1) )
print('string_brute_force_check : \t ',string_brute_force_check(200001, 1) )

# Algorithm construction and logic approach !! I must go from above, see if the count digit is bellow S
# if we are bellow go up, if the count(digit) > number go down

def algorithm_logic():
    S, s = 0, ''
    i = 1
    d = 1
    while S < 10**7 :
        S += str(i).count(str(d))
        if i == S :
            print(str(i)+'.     ', S)
        i+=1

# algorithm_logic TESTING

def test_main_function( up_lim , d  ):
    S, s = 0, ''
    i = 1
    incorrect = 0
    while S < up_lim :
        S += str(i).count(str(d))
        if S != f(i, d, D  ) :
            print('i=  '+str(i)+'        corrrect = ', S , '             f = ', f(i, d, D))
            incorrect +=1
        i+=1
    print('Incorrect numbers : ', incorrect)


# test_main_function( 10**4  , 5 )





t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

def interval_check_nr(rng, digit ) :
    S = set()
    for n in range(rng, rng+100):
        g = f(n, digit, D)
        if n == g :
            # print(str(n) + '.        f() = ', g,'      ', n-g )
            S.add(n)
    return S

print( interval_check_nr(199961, 1) )
print( interval_check_nr(200003, 1) )
print( interval_check_nr(1599978 , 1) )
print( interval_check_nr(13199900 , 1 ) )
print( interval_check_nr(117463825, 1  ) )
#
# 1   Sum = 1
# 199981   Sum = 199982
# 199982   Sum = 399964
# 199983   Sum = 599947
# 199984   Sum = 799931
# 199985   Sum = 999916
# 199986   Sum = 1199902
# 199987   Sum = 1399889
# 199988   Sum = 1599877
# 199989   Sum = 1799866
# 199990   Sum = 1999856
# 200000   Sum = 2199856
# 200001   Sum = 2399857
# 1599981   Sum = 3999838
# 1599982   Sum = 5599820
# 1599983   Sum = 7199803
# 1599984   Sum = 8799787
# 1599985   Sum = 10399772
# 1599986   Sum = 11999758
# 1599987   Sum = 13599745
# 1599988   Sum = 15199733
# 1599989   Sum = 16799722
# 1599990   Sum = 18399712
# 2600000   Sum = 20999712
# 2600001   Sum = 23599713
# 13199998   Sum = 36799711
# 35000000   Sum = 71799711
# 35000001   Sum = 106799712
# 35199981   Sum = 141999693
# 35199982   Sum = 177199675
# 35199983   Sum = 212399658
# 35199984   Sum = 247599642
# 35199985   Sum = 282799627
# 35199986   Sum = 317999613
# 35199987   Sum = 353199600
# 35199988   Sum = 388399588
# 35199989   Sum = 423599577
# 35199990   Sum = 458799567
# 35200000   Sum = 493999567
# 35200001   Sum = 529199568
# 117463825   Sum = 646663393
# 500000000   Sum = 1146663393
# 500000001   Sum = 1646663394
# 500199981   Sum = 2146863375
# 500199982   Sum = 2647063357
# 500199983   Sum = 3147263340
# 500199984   Sum = 3647463324
# 500199985   Sum = 4147663309
# 500199986   Sum = 4647863295
# 500199987   Sum = 5148063282
# 500199988   Sum = 5648263270
# 500199989   Sum = 6148463259
# 500199990   Sum = 6648663249
# 500200000   Sum = 7148863249
# 500200001   Sum = 7649063250
# 501599981   Sum = 8150663231
# 501599982   Sum = 8652263213
# 501599983   Sum = 9153863196
# 501599984   Sum = 9655463180
# 501599985   Sum = 10157063165
# 501599986   Sum = 10658663151
# 501599987   Sum = 11160263138
# 501599988   Sum = 11661863126
# 501599989   Sum = 12163463115
# 501599990   Sum = 12665063105
# 502600000   Sum = 13167663105
# 502600001   Sum = 13670263106
# 513199998   Sum = 14183463104
# 535000000   Sum = 14718463104
# 535000001   Sum = 15253463105
# 535199981   Sum = 15788663086
# 535199982   Sum = 16323863068
# 535199983   Sum = 16859063051
# 535199984   Sum = 17394263035
# 535199985   Sum = 17929463020
# 535199986   Sum = 18464663006
# 535199987   Sum = 18999862993
# 535199988   Sum = 19535062981
# 535199989   Sum = 20070262970
# 535199990   Sum = 20605462960
# 535200000   Sum = 21140662960
# 535200001   Sum = 21675862961
# 1111111110   Sum = 22786974071

print('\n---------------------------------')
# def find_range(nr_len, d) :
#     n = 10**(nr_len-1)
#     Nrs, Diff  = [] , []        # Nrs - number list, Diff - differences used to establish monotony
#     # Construct the initial list :
#     for h in range(4):
#         g = f(n+h, d, D)
#         Nrs.append(n+h)
#         Diff.append(n+h-g )
#     n+=5
#     print ('------------------------------------     --- Nrs, Diff : \t', Nrs, '         ', Diff ,'\n')
#     iter = 0
#     while len(str(n)) == nr_len :
#         iter+=1
#         Diff, Nrs = Diff[-5::], Nrs[-5::]
#         # OBS : the monotony is tested to see if the number of digits has inflection points =>
#         # this means that it found a matching n with the n nr of digits
#         if monotonic(Diff) == True :
#             n *= 2
#             g = f(n, d, D)
#             Nrs.append(n) ; Diff.append((n-g))
#             print('n = ', n , '        g monoton TRUE = ', g, '       Nrs =', Nrs[-5::],'           Diff =' ,Diff[-5::] ,'        iter=', iter)
#
#         if monotonic(Diff) == False :
#             li, hi = find_elem(Diff)     # is the index of the non-monotonic elements
#             low, high = Nrs[li], Nrs[hi]
#             print('n = ', n , '        g monoton False = ', g, '       Nrs = ', Nrs[-5::],'        Diff = ' ,Diff[-5::] ,'       low, high = ', low, high ,'        iter=', iter)
#             return low, high
#     return False


    # start_nr = binary_search(low, high, d)
    # print('STASRT NUMBER : \t',start_nr)
    #
    # for u in range(start_nr, start_nr+1000) :
    #     if f(u, d, D) == u :
    #         print('chosen number = ', u)
    #         SUM += u



#     return print('\nAnswer : \t', SUM)
#
# first_solution()



# def second_solution() :




# for n in range(199900, 200100 ) :
#     print('n = ', n,'        f(n,1) = ' ,  f(n, 1, D) )

def find_numbers() :
    SUM = 0
    Nrs = { 1 : {1} , 2: {28263827 , 242463827 , 528263827 , 10028263827, 10242463827, 10528263827 } }
    for i in range(1, 10**6+1, 2) :
        print('iter = ', i )
        low, high = i*100000, (i+1)*100000
        # print(' low, high = ', low, high)
        # digits :
        for d in range(1, 10) :
            seeked_nr = binary_search(low, high, d)
            if seeked_nr  != False :
                # print('seeked_number = ', seeked_nr)
                ns = interval_check_nr( seeked_nr, d )
                # print(ns)
                if d not in Nrs : Nrs[d] = set()
                Nrs[d] = Nrs[d].union(ns)
                # print(Nrs[d])
    print('\n--------- RESULTS -------------')
    for k, v in Nrs.items() :
        SUM += sum(Nrs[k])
        print( sum(Nrs[k]) , ' digit',k ,'   Vals=', len(Nrs[k]),'  ', Nrs[k] )

    return print('\nTotal Sum = ' , SUM )


# find_numbers()


# zzz.Star_Wars()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)/3600, 2 ), 'hours\n\n')

print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1, AMAZING, INSTANT   --------------------------')
t1  = time.time()

# === Thu, 22 Dec 2016, 20:57, gjanee, USA
# Python, 0.067s

# For fixed d, the function f(n,d) is quite interesting: it's
# self-similar, or fractal.  Consider f(n,d) over domain 0 <= n < 10^e
# for e > 0, and divide that domain into 10 subdomains each of width
# 10^(e-1) corresponding to leading digits 0,...,9.  f exhibits the
# same behavior over each subdomain (because the pattern of digits d
# is the same in each subdomain) except at leading digit d where the
# extra leading digits d cause f to "pop up," i.e., to rise faster
# over that subdomain.  These "pop ups" occur at each scale.  It is
# easily shown by induction that f(10^e-1,d) = e*10^(e-1) for e > 0
# (coincidence, or a connection to a derivative?).
#
# The relationship between f(n,d) and the line y = n is also
# interesting.  f(n,d) starts out equal to the line and immediately
# falls below, but at each scale its "pop up" region rises higher and
# higher and eventually begins crossing the line.  The crossings
# represent possible match locations.  Since f(10^e,d) > 10^e for all
# e >= 11, we can use 10^11 as an upper bound.
#
# We solve the problem for the domain 0 <= n < 10^11 by recursively
# examining smaller and smaller subdomains.  Consider an arbitrary
# subdomain of width 10^e (suitably aligned, of course) with
# p digits d in its prefix.  (For example, if d = 1, for the subdomain
# 121711xxx of width 10^3, the prefix is "121711" and p = 4.)  Then
# the subdomain augments f by e*10^(e-1) + p*10^e.  In this way we can
# calculate the contribution any arbitrary subdomain makes to f.
#
# We employ two heuristics to remove the vast majority of subdomains
# from consideration.  Consider an aligned subdomain l <= n < r.  Then
# the subdomain is discarded if f(l,d) < l and f(r,d) < l (i.e., if f
# is below the line and cannot possibly have crossed it in the
# subdomain) or if f(l,d) > r and f(r,d) > r (i.e., if f is above the
# line and must have stayed above it over the entire subdomain).

def matchSum (d, n, b, f, p):
  # d: digit
  # n: domain width 10^n
  # b: domain's lower bound
  # f: f(b-1,d)
  # p: common prefix sum over domain
  # returns sum of matches found in the domain
  s = 0
  if n == 1:
    fi = f
    for i in range(10):
      fi += p
      if i == d: fi += 1
      if fi == b+i: s += b+i
  else:
    m = n-1
    l = b
    fl = f
    for i in range(10): # for each subdomain [l, r)
      r = l+10**m
      fr = fl+m*10**(m-1)+p*10**m
      if i == d: fr += 10**m
      if fr >= l and fl <= r: s += matchSum(d, m, l, fl, p+1 if i == d else p)
      l = r
      fl = fr
  return s

print (sum(matchSum(d, 11, 0, 0, 0) for d in range(1, 10)))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

class Problem():
    def __init__(self):
        self.found = None

    def solve(self):
        count = 0
        for digit in range(1, 10):
            solution_sum = self.s(digit)
            print(digit, solution_sum)
            count += solution_sum
        print(count)

    def s(self, digit):
        self.found = []
        self.binary_search(1, 10**11, digit)
        return sum(self.found)

    def f(self, n, digit):
        count = 0
        factor = 1
        while n // factor != 0:
            lower_number = n - (n // factor) * factor
            curr_number = (n // factor) % 10
            higher_number = n // (factor * 10)
            if curr_number < digit:
                count += higher_number * factor
            elif curr_number == digit:
                count += higher_number * factor + lower_number + 1
            else:
                count += (higher_number + 1) * factor
            factor *= 10
        return count

    def binary_search(self, lower, upper, digit):
        if lower + 1 == upper:
            if self.f(lower, digit) == lower:
                self.found.append(lower)
            return
        middle = (lower + upper) // 2
        lower_value = self.f(lower, digit)
        upper_value = self.f(upper, digit)
        middle_value = self.f(middle, digit)
        if middle_value >= lower and middle >= lower_value:
            self.binary_search(lower, middle, digit)
        if upper_value >= middle and upper >= middle_value:
            self.binary_search(middle, upper, digit)

    def f_naive(self, n, digit):
        return sum([self.count_naive(i, digit) for i in range(1, n+1)])

    def count_naive(self, n, digit):
        count = 0
        while n > 0:
            n, r = divmod(n, 10)
            if r == digit:
                count += 1
        return count


problem = Problem()
problem.solve()



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 5,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 6,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
