#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Rounded Square Roots        -       Problem 255

We define the rounded-square-root of a positive integer n as the square root of n rounded to the nearest integer.

The following procedure (essentially Heron's method adapted to integer arithmetic) finds the rounded-square-root of n:

Let d be the number of digits of the number n.
If d is odd, set x_0 = 2×10**(d-1)⁄2.
If d is even, set x_0 = 7×10**(d-2)⁄2.
Repeat:

x_(k+1) = floor( ( x_k + ceil( n/x_k ))  /2 )

until x_(k+1) = x_k.

As an example, let us find the rounded-square-root of n = 4321.
n has 4 digits, so x0 = 7×10(4-2)⁄2 = 70.

x_1 = floor( ( 70 + ceil( 4321/70 )) /2  ) =66
x_2  = floor( ( 66 + ceil( 4321/66 ))  /2 ) =66

Since x2 = x1, we stop here.
So, after just two iterations, we have found that the rounded-square-root of 4321 is 66 (the actual square root is 65.7343137…).

The number of iterations required when using this method is surprisingly low.
For example, we can find the rounded-square-root of a 5-digit integer (10,000 ≤ n ≤ 99,999)
with an average of 3.2102888889 iterations (the average value was rounded to 10 decimal places).

Using the procedure described above, what is the average number of iterations required to find
the rounded-square-root of a 14-digit number (10**13 ≤ n < 10**14)?

Give your answer rounded to 10 decimal places.

Note: The symbols ⌊x⌋ and ⌈x⌉ represent the floor function and ceiling function respectively.

'''
import time
from math import ceil, floor, sqrt



def Heron_integer_arithmetic(n):
    d = len(str(n))
    if d%2 == 1 :
        x = 2*10**( (d-1)/2 )
    if d%2 ==0 :
        x = 7*10**((d-2)/2 )
    i1, i2 = x, -16
    cnt=0
    while i1 != i2 :
        cnt+=1
        i1 = x
        x = floor( ( x+ceil((n/x )) )/2 )
        i2 = x
        # print('i1, i2 = ', i1, i2, '        x=',x)

    return x, cnt

print('\nHeron_integer_arithmetic : \t', Heron_integer_arithmetic(4321))


print('\n--------------------------TESTS------------------------------')
t1  = time.time()

# down, up = 10**13+8*10**11+7*10**10+6*10**9+8*10**8+8*10**7+6*10**6+4*10**5 , 10**14
def brute_force_verification(down, up, step) :

    L = up - down
    S=0
    cnt, itr = 0, 0

    for n in range(down, up, step) :
        cnt+=1
        a = Heron_integer_arithmetic(n)
        S+=a[1]
        if a[1] != itr :
            itr = a[1]
            print('n= ', n,'         iter = ' , a[1], '       res = ' , a[0] , '         sqrt(n) =  ' ,  sqrt(n) , '        ' ,  S/cnt )

    print('\nAnswer : \t', round(S/L, 10 ) , '                ',  S/L )
    return round(S/L, 10 )

# down, up, step = 10**4 , 10**5, 10**0
# down, up, step = 10**6, 10**7, 10**0

down, up, step = 6*10**13+7*10**11 , 6*10**13 +8*10**11, 10**0
# down, up, step = 10**13 , 10**14, 10**4

brute_force_verification(down, up, step)

# @2017-10-16 - The value should look something like :  4.447450333333333

# OBS : 2017-02-21 --> Must Do Reverse Engineering on that function
# There are values of 6,5,4
        ####  Boundary
    # 46440.     (215, 3)          215.49941995281566
    # 46441.     (216, 2)          215.5017401321855

# We can see the boundary between < 15.5 and >15.5

# It seems that there are 2 types of changes : 1. based on boundaries as above

# 2. Anomalies which I must investigate !!! as :
#             47400.     (218, 2)          217.7154105707724
#             47401.     (218, 3)          217.71770713472068
#
#             46600.     (216, 2)          215.87033144922904
#         46601.     (216, 3)          215.87264764207623
# 45800.     (214, 2)          214.00934559032697          2.938632999078238
# 45801.     (214, 3)          214.0116819241417          2.938634713144517
# 45399.     (213, 2)          213.0704108974308          2.9441242937853107
# 45400.     (213, 2)          213.07275752662517          2.944097624360894

# https://www.youtube.com/watch?v=iaBEKo5sM7w

'''  @2019-01-27, 12:11 - STRATEGY : - An O(n^1/2) algorithm
1.  iterate over sqrt numbers .
2. Try to position yourself to .5 and see the numbers of iterations there.
3. ... The algorithm becomes obvious
n=  10000000000000          iter =  6        res =  3162278          sqrt(n) =   3162277.6601683795          6.0
n=  10000005311561          iter =  7        res =  3162278          sqrt(n) =   3162278.4999998026          6.000000188268536
n=  10000005311563          iter =  6        res =  3162279          sqrt(n) =   3162278.5000001187          6.00000037653693
n=  10000011636119          iter =  7        res =  3162279          sqrt(n) =   3162279.4999998026          6.000000257817898
n=  10000011636121          iter =  6        res =  3162280          sqrt(n) =   3162279.5000001187          6.000000343757138
n=  10000017960679          iter =  7        res =  3162280          sqrt(n) =   3162280.4999998026          6.000000278385897
n=  10000017960681          iter =  6        res =  3162281          sqrt(n) =   3162280.5000001187          6.000000334063039
n=  10000024285241          iter =  7        res =  3162281          sqrt(n) =   3162281.4999998026          6.0000002882409
n=  10000024285243          iter =  6        res =  3162282          sqrt(n) =   3162281.5000001187          6.000000329418143
n=  10000030609805          iter =  7        res =  3162282          sqrt(n) =   3162282.4999998026          6.000000294023425
n=  10000030609807          iter =  6        res =  3162283          sqrt(n) =   3162282.5000001187          6.000000326692673
n=  10000036934371          iter =  7        res =  3162283          sqrt(n) =   3162283.4999998026          6.00000029782556
n=  10000036934373          iter =  6        res =  3162284          sqrt(n) =   3162283.5000001187          6.000000324900593
n=  10000043258939          iter =  7        res =  3162284          sqrt(n) =   3162284.4999998026          6.000000300515916
n=  10000043258941          iter =  6        res =  3162285          sqrt(n) =   3162284.5000001187          6.00000032363251

10**6, 10**7            Answer : 	 3.6100002222                  3.6100002222222223



n=  30500000000000          iter =  4        res =  5522681          sqrt(n) =   5522680.50859363          4.0
n=  30500006372983          iter =  5        res =  5522681          sqrt(n) =   5522681.08557637          4.000000156912367
n=  30500010950443          iter =  4        res =  5522682          sqrt(n) =   5522681.500000068          4.418015927025425
n=  30500017418347          iter =  5        res =  5522682          sqrt(n) =   5522682.085576446          4.262795358090216
n=  30500021995807          iter =  4        res =  5522683          sqrt(n) =   5522682.500000068          4.416212034584045
n=  30500028463713          iter =  5        res =  5522683          sqrt(n) =   5522683.08557652          4.321634801417693
n=  30500033041173          iter =  4        res =  5522684          sqrt(n) =   5522683.500000068          4.415614166736328
n=  30500039509081          iter =  5        res =  5522684          sqrt(n) =   5522684.085576596          4.347575299269166
n=  30500044086541          iter =  4        res =  5522685          sqrt(n) =   5522684.500000068          4.41531585761478
n=  30500050554451          iter =  5        res =  5522685          sqrt(n) =   5522685.085576671          4.362180585005649
n=  30500055131911          iter =  4        res =  5522686          sqrt(n) =   5522685.500000068          4.415137062541927
n=  30500061599823          iter =  5        res =  5522686          sqrt(n) =   5522686.085576746          4.371548155722003
n=  30500066177283          iter =  4        res =  5522687          sqrt(n) =   5522686.500000068          4.415017938783949
n=  30500072645197          iter =  5        res =  5522687          sqrt(n) =   5522687.085576821          4.3780671228950325
n=  30500077222657          iter =  4        res =  5522688          sqrt(n) =   5522687.500000068          4.414932881486674
n=  30500083690573          iter =  5        res =  5522688          sqrt(n) =   5522688.085576896          4.382865351120665
n=  30500088268033          iter =  4        res =  5522689          sqrt(n) =   5522688.500000068          4.414869101989969
n=  30500094735951          iter =  5        res =  5522689          sqrt(n) =   5522689.085576971          4.386544709024511



n=  50700000000000          iter =  3        res =  7120393          sqrt(n) =   7120393.247567159          3.0
n=  50700002522583          iter =  4        res =  7120393          sqrt(n) =   7120393.4247050565          3.00000039641891
n=  50700003594843          iter =  3        res =  7120394          sqrt(n) =   7120393.500000053          3.298277199233124
n=  50700016763371          iter =  4        res =  7120394          sqrt(n) =   7120394.424705067          3.0639645174013914
n=  50700017835631          iter =  3        res =  7120395          sqrt(n) =   7120394.500000053          3.1202379596080476
n=  50700031004161          iter =  4        res =  7120395          sqrt(n) =   7120395.424705078          3.0691688103035974
n=  50700032076421          iter =  3        res =  7120396          sqrt(n) =   7120395.500000053          3.1002848759129056
n=  50700045244953          iter =  4        res =  7120396          sqrt(n) =   7120396.424705088          3.071097011171677
n=  50700046317213          iter =  3        res =  7120397          sqrt(n) =   7120396.500000053          3.0926014246020928
n=  50700059485747          iter =  4        res =  7120397          sqrt(n) =   7120397.424705098          3.0721019932371028
n=  50700060558007          iter =  3        res =  7120398          sqrt(n) =   7120397.500000053          3.0885316439074417
n=  50700073726543          iter =  4        res =  7120398          sqrt(n) =   7120398.42470511          3.072718734788382
n=  50700074798803          iter =  3        res =  7120399          sqrt(n) =   7120398.500000053          3.086011535692469
n=  50700087967341          iter =  4        res =  7120399          sqrt(n) =   7120399.42470512          3.0731357894160314

n=  60700000415165          iter =  5        res =  7791020          sqrt(n) =   7791020.498956796          4.000002408675084
n=  60700000431421          iter =  4        res =  7791021          sqrt(n) =   7791020.500000048          4.037680044133123
n=  60700015997207          iter =  5        res =  7791021          sqrt(n) =   7791021.498956796          4.001016239833851
n=  60700016013463          iter =  4        res =  7791022          sqrt(n) =   7791021.500000048          4.002030291509695
n=  60700031579251          iter =  5        res =  7791022          sqrt(n) =   7791022.498956796          4.00102956840143
n=  60700031595507          iter =  4        res =  7791023          sqrt(n) =   7791022.500000048          4.001543510552196
n=  60700047161297          iter =  5        res =  7791023          sqrt(n) =   7791023.498956796          4.001034089434943
n=  60700047177553          iter =  4        res =  7791024          sqrt(n) =   7791023.500000048          4.001378282562085

'''




t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()





def first_solution(down, up) :

    down_lim, up_lim = down, up

    a, z = sqrt(down)  ,  sqrt(up)




    SUM = Heron_integer_arithmetic(down)[1]

    print('a=  ', a, '      z= ', z ,'      SUM= ', SUM)

    i = a
    while True :
        print('-----------          i= ', i )
        if i > z - 1 :
            print('Reached the limit ...')
            # print('i = ',i ,'    i^2 = ', i*i  ,'     down = ', down   )

            up = up_lim-1
            diff = up - down+1
            SUM += iter0 * diff
            # print('k = ', k, '         k^2= ', k*k, '       down = ', down, '     up= ', up, '     diff =' , diff, '    iter= ', iter0 ,'      SUM= ', SUM )
            break

        # k = ceil(i) + 0.499999
        k = ceil(i) + 0.47
        j = floor(k*k)
        up = j
        diff = up - down+1
        iter0 = Heron_integer_arithmetic(down)[1]
        SUM += iter0 * diff
        # print('k = ', k, '         k^2=  ', k*k, '       down = ', down, '     up= ', up, '     diff =' , diff, '    iter= ', iter0 ,'      SUM= ', SUM )

        while sqrt(j) < floor( k ) + 0.5 :
            v, iter1 = Heron_integer_arithmetic(j)
            SUM += iter1

            # print('             j = ',  j , '    v=' ,v, '     iter =', iter1,'        sqrt(j) = ', sqrt(j),'      sum= ', SUM )

            j+=1
        down = j
        # print('     down = ',  down )

        i+=1


    print('down_lim = ', down_lim,  '       up_lim = ', up_lim ,'         ', up_lim-down_lim  )
    print('\nANSWER : ',  SUM/(up_lim-down_lim)  )

    return SUM/(up_lim-down_lim)



# down, up = 10**6, 10**7
down, up = 3*10**13+5*10**11 , 3*10**13 +6*10**11

first_solution(down, up)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
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
