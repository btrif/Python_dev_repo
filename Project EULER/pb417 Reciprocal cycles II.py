#  Created by Bogdan Trif on 23-05-2018 , 11:38 AM.
# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
                    Reciprocal cycles II            -           Problem 417

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Unit fractions whose denominator has no other prime factors than 2 and/or 5 are not considered to have a recurring cycle.
We define the length of the recurring cycle of those unit fractions as 0.

Let L(n) denote the length of the recurring cycle of 1/n.

You are given that ∑L(n) for 3 ≤ n ≤ 1 000 000 equals 55535191115.

Find ∑L(n) for 3 ≤ n ≤ 100 000 000

'''
import time, zzz


print('\n--------------------------TESTS------------------------------')
t1  = time.time()


LINKS
https://en.wikipedia.org/wiki/Cyclic_number
https://en.wikipedia.org/wiki/Repeating_decimal#Cyclic_numbers
https://stackoverflow.com/questions/11029001/finding-cycles-in-decimal-expansion-of-rational-numbers
https://www.mlwright.org/docs/cycles.pdf
http://mathworld.wolfram.com/DecimalExpansion.html              !!!!!!!!!!
https://hr.userweb.mwn.de/numb/period.html

@2018 KEY OBSERVATION :     (http://mathworld.wolfram.com/DecimalExpansion.html)
It is possible to find the period without actually calculating the whole decimal expansion and cycle
EXAMPLES :
if we take 84 --> it has a cycle of 6 --> 0.01(190476) because 84 = [ 2, 2, 3, 7  ] and 2 (no cycle) ; 3(cycle = 1) and 7 is biggest cycle
    7 -->0.(142857) => the max cycle is the cycle of 7 is 6 length .
if we take 77 --> it has a cycle of 6 -> 0.0(129870) because 77=[7, 11] ; 11 cycle is 0.0(90) = 2
and 7 has the largest cycle which is 6 -->(0.142857) => take the cycle of 7

17 --> (0.0588235294117647) = 16 cycle =>
the number :

187 = 17*7 --> cycle = 0.(0053475935828877)  = 16
but we add one more number : the cycles becomes a multiple of the original cycle
17*11*7= 1309 --> cycle is : 000763941940412528647822765469824293353705118411 = length 48=16*3

221 = 17 * 13 --> cycle = 1/221: 0.(004524886877828054298642533936651583710407239819) = 48
1/13:       0.(076923)      --> cycle of 6  => 6*16 = 96 / 2 = 48


OBSERVATION II :
(10**10-1)//11       =       909090909.0 = 2
in general , for a prime :
p = 13,             (10**(p-1)-1)//p


def _wolfram_algo(p):       # Made by Bogdan Trif @ 2018-05-23
    ''':Description: finds the period cycle of decimals of a fraction of the type 1/n
        :Example:   1/7 = 0.(142857) = 6 period  ;
                http://mathworld.wolfram.com/DecimalExpansion.html::                 '''


    i, cnt = 0, 0
    S, T = set(), []
    m = 10**i % p

    while m not in S :
        S.add(m)
        T.append(m)
        i+=1
        cnt+=1
        m = 10**i % p
#         print(m,'  ', S,'   ', T)

    print('cnt = ', cnt, T.index(m) )
    return cnt - T.index(m)

# _wolfram_algo(7*11*13*17*19)
_wolfram_algo(19)


def digits(p) :

    return (10**(p-1)-1)//p

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()





# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
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

