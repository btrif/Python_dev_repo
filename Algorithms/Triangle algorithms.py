# ====Wed, 31 Dec 2008, 03:31, Jepso, Finland
# I used Euclid's formula for generating the triplets: a = 2mn, b = m2 - n2, c = m2 + n2.
# In order for a right-angle triangle to allow tiling, c % (b - a) == 0 must hold.
# If this holds for the primitive triangle, it's true for all (k*a, k*b, k*c).
#
# Then I noticed a pattern between such (m, n) pairs for which this holds.
# If we start from (m0, n0) = (2, 1), we can get all (m, n) pairs that generate correct triangles
# with the following recursive formula: (mi, ni) = (2mi-1 + ni-1, mi-1).
#
# The code below runs in 0.020 seconds.

from math import sqrt, cos, sin, pi

p_max = 100 * 10**6
cnt = 0

m, n = 2, 1
while True:
    a = 2 * m * n
    b = m*m - n*n
    c = m*m + n*n
    p = a + b + c
    if p >= p_max:
        break
    cnt += p_max // p
    print (m, n, cnt)
    m, n = 2*m + n, m
print (cnt)



def compute_triangle_angles( sides ):   # o(^_^)o #  Made by Bogdan Trif @ 2017-02-19, 12:20
    ''':Description: given a triangle with sides a,b,c the function computes all its angles.
        It uses the LAW OF SINES , where A,B,C are the angles opposed to corresponding sides a,b,c
        sin(A)/a =sin(B)/b =sin(C)/c
        and the LAW OF COSINES c**2 = a**2 + b**2 - 2*a*b * cos(C)
    :returns: A,B,C, the three corresponding angles    '''
    from math import sqrt, cos, sin, pi, acos, asin
    a, b, c = sides[0], sides[1], sides[2]
    C = acos((a**2+b**2-c**2)/(2*a*b) )*180/pi
    A = asin(( a*sin(C*pi/180) )/c )*180/pi
    B = asin(( b*sin(C*pi/180) )/c )*180/pi
    return A, B, C

print('\ncompute_triangle_angles :\t', compute_triangle_angles( (19, 261, 271) )  )


print('\n---------------- Triangle Primitive Triplets of 120 degrees ------------------ ')

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

TPT = triangle_primitive_triplets_120_gen(  )
for i in range(40):
    print(next(TPT))


print('\n---------------- Triangle Primitive Triplets of 60 degrees ------------------ ')

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
            if gcd(m,n)==1 and (m-n)%3 !=0  :         #!!!! if we omit the %3 condition we will get duplicates !!!
                a = 2*m*n + m**2
                b = 2*m*n + n**2
                c = m**2+n**2+m*n
                cnt+=1
                print(str(cnt)+'.         '  , a, b, c ,'       sum =',  a+b+c ,'            m,n =',m, n)
                yield a, b, c
        m+=1

TPT60 = triangle_primitive_triplets_60_gen(  )
for i in range(40):
    f = next(TPT60)
    print(f,'     angles : ', compute_triangle_angles(f))



############ HERONIAN TRIANGLES ###################

def Heron_area_perimeter(a,b,c):
    s= (a+b+c)/2
    return (s*(s-a)*(s-b)*(s-c))**(1/2), s*2

from math import gcd
def gcd3(a, b, c):
    return gcd(gcd(a, b), c)


def compute_Heron_area_after_coordinates( p1, p2, p3 ) :
    a = sqrt( (p1[0]-p2[0])**2 +  ( p1[1]-p2[1] )**2  )
    b = sqrt( (p1[0]-p3[0])**2 +  ( p1[1]-p3[1] )**2 )
    c = sqrt(  (p2[0]-p3[0])**2 +  ( p2[1]-p3[1] )**2 )
    s = (a+b+c)/2

    return sqrt( s*(s-a)*(s-b)*(s-c) )


def Heron_area_perimeter(a,b,c):
    s= (a+b+c)/2
    return (s*(s-a)*(s-b)*(s-c))**(1/2)

angleC = lambda a,b,c : acos( ( a**2 + b**2 - c**2) / (2*a*b) )*180/pi

angleA =  lambda a,b,c : acos(( b**2 + c**2 - a**2) / (2*b*c))*180/pi

angleB =  lambda a,b,c : acos( (c**2 + a**2 - b**2) / (2*c*a))*180/pi

CE = lambda a,b,c : (sqrt( (a*b)*(a+b+c)*(a+b-c)) )/ (a+b)
BG = lambda a,b,c : (sqrt( (a*c)*(a+c+b)*(a+c-b) ))/ (a+b)

y =  lambda B_G, c, angleB :   sqrt( B_G*B_G + c*c - (2*B_G*c * cos( (angleB*pi)/(2*180) ) ))

x =  lambda C_E, a, angleC :   sqrt(C_E*C_E + a*a - (2*C_E*a * cos( (angleC*pi)/(2*180) ) ))

GE =  lambda x, y, angleA :   sqrt(x*x + y*y - (2*x*y * cos( (angleA*pi)/180 ) ))



def Heronian_angles_area_after_coordinates( p1, p2, p3 ) :
    from math import sqrt, cos, sin, pi, acos, asin
    a = sqrt( (p1[0]-p2[0])**2 +  ( p1[1]-p2[1] )**2  )
    b = sqrt( (p1[0]-p3[0])**2 +  ( p1[1]-p3[1] )**2 )
    c = sqrt(  (p2[0]-p3[0])**2 +  ( p2[1]-p3[1] )**2 )
    angleC =  acos( ( a**2 + b**2 - c**2) / (2*a*b) )*180/pi
    angleA =  acos(( b**2 + c**2 - a**2) / (2*b*c))*180/pi
    angleB =  acos( (c**2 + a**2 - b**2) / (2*c*a))*180/pi
    return angleC, angleB, angleA , angleC+ angleB+ angleA

Heronian_angles_area_after_coordinates((0,0) , (6, 6), (2, -1) )
