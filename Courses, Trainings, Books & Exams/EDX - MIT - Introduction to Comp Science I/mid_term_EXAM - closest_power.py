'''
base: base of the exponential, integer > 1
num: number you want to be closest to, integer > 0
Find the integer exponent such that base**exponent is closest to num.
Note that the base**exponent may be either greater or smaller than num.
In case of a tie, return the smaller value.
Returns the exponent.
'''

'''
base: base of the exponential, integer > 1
num: number you want to be closest to, integer > 0
Find the integer exponent such that base**exponent is closest to num.
Note that the base**exponent may be either greater or smaller than num.
In case of a tie, return the smaller value.
Returns the exponent.
'''

def closest_power(base, num):

    if ( num == 1 or base > num ):
        return 0

    else:
        a = 2
        minv = abs(base - pow(num, 1/(a)))

        if minv < abs(base - pow(num, 1/(a+1))):

            while  minv < abs(base - pow(num, 1/(a+1))) :
                temp_minv = minv
                minv = abs(base - pow(num, 1/(a+1)))
                if abs((base**(a-1)) - num) == abs( base**(a) - num ):
                    return a-1
                elif temp_minv < minv :
                    return a
                a-=1
                #print(minv)
            if base**(a-1) == 1:
                return 1
            elif abs((base**a) - num) < abs( base**(a-1) - num ):
                return a
            else:
                return a+1

        elif   minv > abs(base - pow(num, 1/(a+1))) :
            while  minv > abs(base - pow(num, 1/(a+1))) :
                minv = abs(base - pow(num, 1/(a+1)))
                a +=1
                #print(minv)
            if abs((base**a) - num) == abs( base**(a-1) - num ) :
                return a-1
            elif minv < abs(base - pow(num, 1/(a+1))) :
                return a


A = closest_power(11,66)
print(A)



'''
    if num == 1:
        return 0
    i=1
    while base**i <= int(pow(num,1.0/2)) :
        i+=1

        if ( abs(base**i - num) < abs(base **(i+1)-num) ):
            return i
        else: return i+1

    while base**i  >= int(pow(num,1.0/2)) :
        i+=1

        if ( abs(base**i - num) < abs(base **(i+1)-num) ):
            return i
        else: return i+1

'''

