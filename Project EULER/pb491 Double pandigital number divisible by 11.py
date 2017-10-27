#  Created by Bogdan Trif on 16-10-2017 , 6:17 PM.
# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
Double pandigital number divisible by 11        -       Problem 491

We call a positive integer double pandigital if it uses all the digits 0 to 9 exactly twice (with no leading zero).
For example, 40561817703823564929 is one such number.

How many double pandigital numbers are divisible by 11?


'''
import time, zzz

import itertools

print('\n--------------------------TESTS------------------------------')
t1  = time.time()

def brute_force(lim):
    cnt = 0
    for x in itertools.product(range(0, lim), repeat=lim*2):
        if x[0] != 0 :
            cc = 0
            for c in range(0, lim) :
                if x.count(c) == 2 :
                    cc +=1
            if cc == lim :
                n = int(''.join([str(i) for i in x]))
                if n%11 == 0 :
                    cnt += 1
                    print(str(cnt)+'.       ', n )

    # for i1 in range(1,4) :
    #     for i2 in range(4) :
    #         for i3 in range(4) :
    #             for i4 in range(4) :
    #                 for i5 in range(4) :
    #                     for i6 in range(4) :
    #                         for i7 in range(4) :
    #                             for i8 in range(4) :
    #                                 s = str(i1)+str(i2)+str(i3)+str(i4)+str(i5)+str(i6)+str(i7)+str(i8)
    #                                 if s.count('0') ==2 and s.count('1')==2 and s.count('2') ==2 and s.count('3')==2 :
    #                                     n = int(s)
    #                                     if n% 11 == 0 :
    #                                         cnt += 1
    #                                         print(str(cnt)+'.       ', n )
    return print('\nthere are : ', cnt)
brute_force(5)


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




