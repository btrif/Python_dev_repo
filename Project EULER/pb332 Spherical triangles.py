#  Created by Bogdan Trif on 14-10-2017 , 10:18 PM.
# © o(^_^)o  Solved by Bogdan Trif  @       Completed on Sat, 5 May 2018, 12:02
#The  Euler Project  https://projecteuler.net
'''
                Spherical triangles         -           Problem 332

A spherical triangle is a figure formed on the surface of a sphere by three great circular arcs intersecting pairwise in three vertices.

p332_spherical.jpg

Let C(r) be the sphere with the centre (0,0,0) and radius r.
Let Z(r) be the set of points on the surface of C(r) with integer coordinates.
Let T(r) be the set of spherical triangles with vertices in Z(r).
Degenerate spherical triangles, formed by three points on the same great arc, are not included in T(r).
Let A(r) be the area of the smallest spherical triangle in T(r).

For example A(14) is 3.294040 rounded to six decimal places.

Find Sum{ r=1 | r=50}  A(r). Give your answer rounded to six decimal places.
'''
import time, zzz
from itertools import combinations
from math import pi, sqrt, pow, sin, cos, asin, acos, tan, atan, floor, atan2

SPH_Area = lambda r : 4*pi*r**2

print( 'Sphere Area : \t',SPH_Area(14) )


def radians_to_degrees(radians) :
    '''radians_to_degrees, Radians to Degrees ,radians to degrees, RADIANS TO DEGREES, rad_to_deg, rad to deg    '''
    return radians * 180 /pi

def positive_rad(radian) :
    ''':Description: Transform a negative radian to positive radian '''
    if radian < 0 :
        return radian + 2*pi
    else : return radian

def positive_deg(degrees) :
    ''':Description: Transform a negative radian to positive radian '''
    if degrees < 0 :
        return degrees + 360
    else : return degrees

print('\n--------------------------TESTS------------------------------')
t1  = time.time()

def brute_force_integer_lattice_points_on_sphere(R) :
    epsilon = 1e-9
    I = set()
    for x in range(0, R+1) :
        y2_z2 = sqrt(R*R - x*x)
        for y in range(0, floor(y2_z2) +1 ) :
            z = sqrt( y2_z2**2 - y*y )
            if abs(z - round(z) ) < epsilon :
                z = round(z)
                print(' x= ', x,'    y= ', y,'     z= ', z ,  '      R =  ',  sqrt(x*x+y*y + z*z) )
                I.add( (x, y, z ) )
                I.add( (x, y , -z ) )
                I.add( ( x, -y, z) )
                I.add( ( x, -y, -z) )

    print('\nInteger points coord : ' , list(I)  )
    return list(I)

# brute_force_integer_lattice_points_on_sphere(14)



t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

### SOURCES :
# https://en.wikipedia.org/wiki/Great-circle_distance
# http://www.mathcaptain.com/geometry/great-circle.html
# http://mathforum.org/library/drmath/view/65316.html     <-- SPHERICAL TRIANGLE AREA
# https://www.movable-type.co.uk/scripts/latlong.html

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  THE MOST IMPORTANT
https://en.wikibooks.org/wiki/Geodesic_Grids/Spherical_geometry_using_vectors

# IDEA SOURCES  - THIS SOLVES THE PROBLEM   :           !!!!!!!!!!!!!!!!!!!!!!
# ==== Sun, 2 Feb 2014, 18:38, ChopinPlover
# Note that
#
# ∠CAB =arccos( (C×A)⋅(B×A) / ( |C×A| |B×A| )
#
# So the area is ER^2 where  :  E=∠CAB+∠ABC+∠BCA−π.


# ===      PROCEDURE   ===          GIVES TRANSFORMATION ERRORS !!!
# STEP 1.     Generate all cartesian coordinates on sphere surface (x,y,z) integer points.
# STEP 2.     Transform from cartesian coordinates to spherical coordinates : (x,y,z) --> (R, theta, phi) (longitude, latitude)
# STEP 3.     Compute great distance circle for all three pairs points of the circle forming the spherical triangle.
# STEP 4.     Calculate the area of the spherical triangle using the three spherical  (a, b, c)  edges of the triangle

### Transformation from Carthesian Coord to Spherical Coord ( Find Latitude phi and Longitude lambda )
phi = lambda z, R : acos( z/R)
print(' phi : ', phi( 5, 14 )  )

theta = lambda x, y : atan(y/x)
print(' theta : ', theta( 5, 14 )  )

print('sin : ', sin(30*pi/180) )



phi1, phi2  = 40.0167,  -33.9333        ###  Latitude
lambda1, lambda2 = 105.2833  , -137.65          ### Longitude
dlambda = abs( lambda1 - lambda2 )          ## Angle Difference in longitude
print( 'dlambda : ', dlambda  )

# print(' captain math : ' , sin(phi1) * sin(phi2) + (cos(phi1) * cos(phi2) * cos(dlambda)) )
# print(' theta :' ,   acos(sin(phi1) * sin(phi2) + (cos(phi1) * cos(phi2) * cos(dlambda))) )

###  First formula ( https://en.wikipedia.org/wiki/Great-circle_distance#Computational_formulas )
dsigma = lambda phi1, phi2, dlambda : acos(   sin(phi1) *sin(phi2) + cos(phi1) * cos(phi2) * cos(dlambda) )


###  SECOND  formula ( https://en.wikipedia.org/wiki/Great-circle_distance#Computational_formulas )
haversine_dsigma = lambda phi1, phi2, dphi , dlambda : 2 * asin( sqrt ( (sin(dphi/ 2))**2 + cos(phi1) * cos(phi2) * (sin(dlambda/ 2))**2  ) )

def haversine_arc_length( φ1, φ2, λ1, λ2  ) :
    ''':Description: where	φ is latitude, λ is longitude, R is earth’s radius (mean radius = 6,371km);
                note that angles need to be in radians to pass to trig functions!
    :param: , c is the angular distance in radians, and a is the square of half the chord length between the points.


                '''
    dφ, dλ = φ2 - φ1 ,    λ2 - λ1
    a = sin(dφ/2) * sin(dφ/2) + cos(φ1) * cos(φ2) * sin(dλ/2) * sin(dλ/2)
    c = 2 * atan2( sqrt(a), sqrt(1-a) )
    return c

# print('dsigma : ' , dsigma(phi1, phi2, dlambda )  )

great_circle_dist = lambda R, dsigma : R * dsigma

#### Spherical excess of Delta - E :
def E_sph_excess_delta(a, b, c) :
    ''':Description: Computes the Spherical Excess of Delta
    :Formula:  E = A+B+C -180 ,   but not used here
    :Formula Used:  **tg(E/4) = sqrt( tan(s/2) *tan((s-a)/2) *tan((s-b)/2) *tan((s-c)/2) )** ,
     where s = (a+b+c) /2 '''
    s = (a+b+c) /2
    X = positive_rad( tan(s/2) *tan((s-a)/2) * tan((s-b)/2) *tan((s-c)/2))
    print('a, b, c = ', a, b,c,'   s=', s, '  X = ', X )

    print( 'X : ' ,   X  )

    return 4 * atan( sqrt(  X   )  )

Area_sph_triangle = lambda R, E : pi * R * R * E / 180      # Formula A_sph_triang = pi * R^2 * E / 180




def Sph_triangle_transf_sides_to_angles( a, b, c  ):
    ''':Description: Transforms the sides of a sperical triangle from sides (angular radians) to angles (radians)  '''
    print(' a, b, c = ', a, b, c )
    print(' test 0 alpha :' ,  ( cos(a) - (cos(b) * cos(c)) ) / ( sin(b) * sin(c)  )     )

    alpha =  acos(  round(  ( cos(a) - (cos(b) * cos(c)) ) / ( sin(b) * sin(c)  ) , 10 ) )

    # print(' acos : ', acos(1.0000))
    beta = acos( round(  ( cos(b) - (cos(c) * cos(a) ) ) / ( sin(c) * sin(a) ) , 10 ) )

    gamma = acos( round(   ( cos(c) - ( cos(a) * cos(b) ) ) / ( sin(a) * sin(b) ), 10 ) )
    #
    # if output_type == 'deg' :
    #     alpha, beta, gamma =  alpha*180/pi, beta*180/pi, gamma*180/pi

    return alpha, beta, gamma

def Sph_triangle_area_from_angles(alpha, beta, gamma, R) :
    E = radians_to_degrees(alpha+beta+gamma) - 180
    Area = pi * E * R*R  /180
    print('E = ', E,'     Area = ', Area  )
    return Area

def cartesian_to_spherical_coord(x, y, z) :
    ''':Description: Transformation  **Cartesian --> Spherical**    Coord system
    :=:    (x, y, z) --> ( **R**, **φ** (phi, latitude), **λ** (lambda,  longitude)  )
    :ATTENTION: the output is different from Standard Sperical Coodrinates where the output is **(R, θ, φ )**
    :param: x, y, z,  coordinates in Cartesian system
    :return: **R**, latitude (**φ** ), longitude(**λ**)
        Mathematics             Geography/Cartography
        r, radial distance      R + h, radius + altitude
        φ, polar angle          90 - φ, colatitude (latitude = 90 - colatitude)
        θ, azimuthal angle      λ,  longitude
        radians                 degrees = radians * 360 / 2π

                            '''

    r = sqrt(x*x + y*y + z*z)
    # h = r - R       # Height above ground
    # λ = arctan(y / x) * 360 / 2π
    λ = atan2( y, x) #* 360 / 2*pi        # so as to account for quadrant or div-by-zero issues
    # φ = 90 - arccos(z / r) * 360 / 2π
    φ = asin( z / r) #* 360 / (2*pi)

    # if x ==0 :
    #     x = 1e-14
    # R = sqrt(x*x+y*y+z*z)
    # λ = acos(z/R)               # longitude
    # phi = atan(y/x)             # latitude

    return r,  φ, λ

def compute_spherical_area(a, b, c, angle_type_in, angle_type_out , R ) :

    if angle_type_in == 'rad' :
        A, B, C = Sph_triangle_transf_sides_to_angles(a, b, c )
        A_rad, B_rad, C_rad = A, B, C
        A_deg, B_deg, C_deg = A_rad*180 /pi, B_rad*180 /pi, C_rad*180 /pi

        E =  A_rad + B_rad + C_rad - pi

    if angle_type_in == 'deg' :
        a, b, c =  a/180*pi, b/180*pi, c/180*pi
        A_rad, B_rad, C_rad = Sph_triangle_transf_sides_to_angles(a, b, c )
        A_deg, B_deg, C_deg = A_rad*180 /pi, B_rad*180 /pi, C_rad*180 /pi

        E = ( A_deg + B_deg + C_deg ) - 180

    print('in degrees :  A_deg = ', A_deg, '    B_deg = ', B_deg, '    C_deg = ', C_deg )
    print('in rads       :  A_rad = ', A_rad, '    B_rad = ', B_rad, '    C_rad = ', C_rad )
    print('spherical excess E = ', E )


    if R != 0 :
        if angle_type_out == 'rad' :
            return E * R * R

        if angle_type_out == 'deg' :
            return E * R * R *pi/ 180
    else : return E


CSA = compute_spherical_area(122.7196,  93.9114 ,  73.6038, 'deg' ,'deg' ,  0 )
print('\ncompute_spherical_area : ', CSA ,'\n'  )


def _get_area( r, a, b, c):
    angle_cab = _get_angle(c, a, b)
    angle_abc = _get_angle(a, b, c)
    angle_bca = _get_angle(b, c, a)
    # print('angle_cab = ', angle_cab, '    angle_abc = ', angle_abc, '    angle_bca = ', angle_bca )
    # print('angle_cab = ', angle_cab*180/pi, '    angle_abc = ', angle_abc*180/pi, '    angle_bca = ', angle_bca*180/pi )
    e = angle_cab + angle_abc + angle_bca - pi
    return e * r**2

def _get_angle( c, a, b ):
    cxa = _cross_product(c, a)
    bxa = _cross_product(b, a)
    # print('cxa =' , cxa ,'      bxa = ', bxa )
    numerator = _inner_product(cxa, bxa)
    denominator = _norm(cxa) * _norm(bxa)
    # print('angle cab = ', acos(numerator/denominator) )
    # print('numerator = ', numerator , '       denominator = ', denominator ,'       num/den = ' , numerator/denominator )
    # if abs(numerator/denominator) >1 :
    #     return 1
    # if denominator == 0 :
    #     return 1e10
    #

    return  acos(numerator/denominator)

def _cross_product( u, v):
    i = u[1] * v[2] - u[2] * v[1]
    j = u[2] * v[0] - u[0] * v[2]
    k = u[0] * v[1] - u[1] * v[0]
    return ( i, j, k)

def _inner_product( u, v):
    return u[0] * v[0] + u[1] * v[1] + u[2] * v[2]

def _norm( v):
    return sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2])



def generate_sph_triangles( R ) :
    min_area = 4* pi * R* R
    AREA = []
    I = brute_force_integer_lattice_points_on_sphere(R)
    # Sph = [ cartesian_to_spherical_coord( i[0], i[1], i[2])  for i in I ]
    # print('Sph : ', Sph ,'\n' )
    comb = combinations( I, 3)
    for cnt, i in enumerate(comb) :
        P1, P2, P3 = i
        print('\n'+str(cnt+1) +'. ---      P1,  P2,  P3   =   ' , P1, P2, P3,'               R = ', R )

        # pairs = list( combinations( (P1, P2, P3) , 2 ) )
        # print('pairs : ', len(pairs), pairs )
        # T, T2 = [], []

        ############## MY FORMULAS from wikipedia are WRONG !!!! or WRONG IMPLEMENTED

        # for cc, J in enumerate(pairs) :
        #     J1, J2 = J
        #
        #     x1, y1, z1 = J1
        #     x2, y2, z2 = J2
        #     C1 = cartesian_to_spherical_coord( x1, y1, z1 )
        #     C2 = cartesian_to_spherical_coord( x2, y2, z2 )
        #     lat1, lon1 = asin(z1 / R), atan2(y1, x1)
        #     lat2, lon2 = asin(z2 / R), atan2(y2, x2)
        #     lambda1, phi1 = C1[1], C1[2]
        #     lambda2, phi2 = C2[1], C2[2]
        #
        #     print(str(cc+1)+'.      J1, J2  = ', J1, J2 ,'       x1, y1, z1 = ', x1, y1, z1 , '     C1 = ', C1 , '     C2 = ', C2 )
        #     print(str(cc+1)+'.       lat1, lon1  = ',  lat1, lon1 ,'        lat2, lon2 = ',  lat2, lon2 )
        #
        #     print('.      lambda1, phi1 = ', lambda1, phi1,'  ;      lambda2, phi2 = ' , lambda2, phi2 )
        #     # dλ = abs( lambda1 - lambda2 )        # latitude
        #     # dφ = abs( phi2 - phi1 )                     #  longitude
        #     # dσ = dsigma( phi1, phi2, dλ )           #   Δσ
        #     # dσ_haversine = haversine_dsigma(phi1, phi2, dφ,  dλ )
        #     Hal = haversine_arc_length( phi1 , phi2, lambda1, lambda2  )
        #     # d = R * dσ        # arc length  ( Great Circle Distance )
        #     # print( 'Δσ =  ', dσ ,'       arc_length =  ' , d )
        #     # print('haversine_arc_length =  ', Hal )
        #     # T.append(dσ)
        #     T.append(Hal )
        # # a, b, c = T
        # a, b, c = T
        #
        #
        #
        # # max_side = max(a, b, c)
        # # if a+b+c-max_side > max_side :
        # a_deg, b_deg, c_deg = list(map( (180/pi).__mul__, T ))
        #
        #
        # print('\na =  ', a, '       b2 =  ', b,  '       c =  ', c )
        # print('a_deg =  ', a_deg, '       b_deg =  ', b_deg,  '       c_deg =  ', c_deg )
        #
        # A, B, C = Sph_triangle_transf_sides_to_angles(a, b, c )
        # print('A, B, C = ', A, B, C )
        # # if  pi <= A+B+C <= 3*pi  :
        #     # print(' a, b, c = ', a, b, c )
        #     # E = E_sph_excess_delta(a, b, c )
        #     # E2 = E_sph_excess_delta(a2, b2, c2)
        #     # Area_Δ = R * R * E

        # Area_Δ = compute_spherical_area(a, b, c, 'rad' , 'rad' , 0 )

        try:
            meng_area =  _get_area( R,  P1,  P2,  P3 )
            print('          meng_area =  ', meng_area   )    # , '     Area_2 = ', Area_2 ,  '\n')

            if 1e-4 < meng_area  < min_area :
                min_area = meng_area
                AREA.append(meng_area)

        except:
            pass

        # meng_area = _get_area(R, P1,  P2,  P3 )

        # A, B, C = Sph_triangle_transf_sides_to_angles(a, b, c)
        # Area_2 = Sph_triangle_area_from_angles( A, B, C, R )
        # Area_2 = 0 #Sph_triangle_area_from_angles( A, B, C, R )

        # print('Sph : Triangle : ', T,'         E_sph_excess_delta =   ' , E*180/pi , '     Area_Δ = ', Area_Δ ) #, '     Area_2 = ', Area_2 ,  '\n')
        # print('Sph : Triangle2 : ', T ,'               '  , '     Area_Δ = ', Area_Δ, Area_Δ*R*R  , '   meng_area =  ', meng_area )# , '     Area_2 = ', Area_2 ,  '\n')


        # AREA.append(Area_Δ)
        # AREA2.append(Area_Δ*R*R)


    print('AREA : ', len(AREA), sorted(AREA) )
    # print('AREA : ', len(AREA2), sorted(AREA2) )
    print('Minimum area : ', min_area )
    return min_area


def main_solution() :
    Total_Sum = 0
    for R in range(1, 51) :

        min_area = generate_sph_triangles(R)
        Total_Sum += min_area

    print( 'Total_Sum : ', Total_Sum  )
    return print('\nANSWER : ' , round(Total_Sum, 6) )

if __name__ == '__main__' :                 #       Total_Sum :  2717.751524886535              ANSWER :  2717.751525
    main_solution()





t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


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




