#  Created by Bogdan Trif on 26-06-2018 , 12:19 PM.
# © o(^_^)o  Solved by Bogdan Trif  @       Completed on Tue, 26 Jun 2018, 18:33
#The  Euler Project  https://projecteuler.net
'''
                          RSA encryption              -               Problem 182

The RSA encryption is based on the following procedure:

Generate two distinct primes p and q.
Compute n=pq and φ=(p-1)(q-1).
Find an integer e, 1<e<φ, such that gcd(e,φ)=1.

A message in this system is a number in the interval [0,n-1].
A text to be encrypted is then somehow converted to messages (numbers in the interval [0,n-1]).
To encrypt the text, for each message, m, c=m^e (mod n ) is calculated.

To decrypt the text, the following procedure is needed: calculate d such that ed=1 mod φ,
then for each encrypted message, c, calculate m=c^d mod n.

There exist values of e and m such that me mod n=m.
We call messages m for which me mod n=m unconcealed messages.

An issue when choosing e is that there should not be too many unconcealed messages.
For instance, let p=19 and q=37.
Then n=19*37=703 and φ=18*36=648.
If we choose e=181, then, although gcd(181,648)=1 it turns out that all possible messages
m (0≤m≤n-1) are unconcealed when calculating m^e mod n.
For any valid choice of e there exist some unconcealed messages.
It's important that the number of unconcealed messages is at a minimum.

Choose p=1009 and q=3643.
Find the sum of all values of e, 1<e<φ(1009,3643) and gcd(e,φ)=1, so that the number of unconcealed messages for this value of e is at a minimum.


'''
import time, zzz
from math import gcd, sqrt

#### Number of unconcealed messages is given by the following formula :     ####
unconcealed = lambda p, q, e : ( gcd( e-1, p-1) +1 ) * ( gcd( e-1, q-1) +1 )

p, q = 19, 37
n = p*q
print('p, q = ', p, q,'           n= ', n )
tot_pq = lambda p, q :  (p-1)*(q-1)



e = 3         #      choose such that :  1<e<φ & gcd(e, φ ) == 1

print('is  1<e<φ & gcd(e, φ ) == 1 :  ' ,  1< e < tot_pq(p, q) and gcd( e, tot_pq(p, q)) == 1  )
print('\ntot_pq = ', tot_pq( p, q) ,'    unconcealed messages : ' , unconcealed(p, q, e) )

def brute_force_unconcealed_messages(n, e ) :
    cnt = 0
    for m in range( n ) :                   #    m in range [ 0,n-1]
        if pow( m, e , n ) == m :

            print('m= ', m ,' =   m^e (mod n) = ',  pow( m, e , n ) ,'           <-- unconcealed message' )
            cnt +=1

    print('\nNr. of unconcealed messages = ', cnt)
    return cnt

brute_force_unconcealed_messages(n , e )



print('\n--------------------------TESTS------------------------------')
t1  = time.time()


# @2018-06-26. 12:55 : Use Chinese Remainder Theorem (CRT) and Extended Euclidian Algorithm ( egcd )
# https://books.google.ro/books?id=8eLiBwAAQBAJ&pg=PA69&lpg=PA69&dq=rsa+unconcealed+messages&source=bl&ots=PRHF-aByWX&sig=tsyk4s2xLt0SwbYtP9XJ6wZj-9M&hl=en&sa=X&ved=0ahUKEwjl-9K5gvHbAhXB1ywKHddEC4EQ6AEISTAE#v=onepage&q=rsa%20unconcealed%20messages&f=false
# http://forums.windowsecurity.com/viewtopic.php?printertopic=1&t=29782&start=0&postdays=0&postorder=asc&vote=viewresult&sid=9bab741eba1b93fbbc3a349233cdadca
# https://math.stackexchange.com/questions/58373/rsa-unconcealed-messages?rq=1
# OBSERVATION : Always for ANY e ,  m = 0, 1, n-1 will be unconcealed

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n================  My FIRST SOLUTION, 5 seconds  ===============\n')
t1  = time.time()

class RSA_encryption(object):
    def __init__(self, p, q ):
        self.p = p
        self.q = q
        self.n = self.p * self.q
        self.phi = (self.p - 1 ) * (self.q - 1 )

    def unconcealed(self, p, q, e ):
        return ( gcd( e-1, self.p-1) +1 ) * ( gcd( e-1, self.q-1) +1 )

    def minimum_unconcealed_messages(self,  p, q  ) :

        Min, cnt, Sum_e = 1e9, 0, 0
        print('n = ', self.n ,'    tot=', self.phi )
        for e in range(2, self.phi ) :          #      choose such that :  1<e<φ & gcd(e, φ ) == 1
            if gcd(e, self.phi) == 1 :
                unco = self.unconcealed( p,q, e)
                if unco < Min :
                    Min = unco
                    cnt, Sum_e = 0, 0
                if unco == Min :
                    cnt+=1
                    Sum_e +=e
                    # print('e=', e , '    unco= ', unco,'     Min=', Min,'     cnt=', cnt, '     Sum_e=', Sum_e  )
        return print('\nANSWER  : \t Sum_e = ', Sum_e )

p, q = 1009, 3643
RSA = RSA_encryption(p, q)
RSA.minimum_unconcealed_messages( p, q )                #   ANSWER  : 	 Sum_e =  399788195976


t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')                # Completed in : 4868.28 ms


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

