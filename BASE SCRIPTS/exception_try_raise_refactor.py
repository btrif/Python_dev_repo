import gmpy2


def get_ratios(L1, L2):
    """ Assumes: L1 and L2 are lists of equal length of numbers
        Returns: a list containing L1[i]/L2[i] """
    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/float(L2[index]))
        except ZeroDivisionError:
            ratios.append(float('NaN')) #NaN= Not a Number
        except:
            raiseValueError('get_ratio scalled with bad arg')
    return ratios

print(get_ratios([2,3,4],[5,6,0]))


print('\n------------------------- Assert ---------------------------------')

def normalize(numbers):
    max_number = max(numbers)
    for i in range(len(numbers)):
        numbers[i] /= float(max_number)
    return numbers

try:
      normalize([0, 0, 0])
except ZeroDivisionError:
      print('Invalid maximum element')

print(normalize([3, 2, 3]))
###################################

def normalize(numbers):
    max_number = max(numbers)
    assert(max_number != 0), "Cannot divide by 0"
    for i in range(len(numbers)):
        numbers[i]  /= float(max_number)
        assert(0.0 <= numbers[i] <= 1.0), "output not between 0 and 1"
    return numbers

# print(normalize([1/2, 4, 2/3, 1/5]))
# print(normalize([0, 0, 0]))

#########################################

print('\n ---------------Test if a variable exists -----------------------')

try:
    thevariable
except NameError:
    print ("well, it WASN'T defined after all!")
else:
    print ("sure, it was defined.")

print('\n -------------------------- isinstance ---------------')
print('------------------This tests if the the value is a int, float or fraction/Decimal --------------------')
from decimal import Decimal
from fractions import Fraction
value = 2/3
print(isinstance(value, (int, float, Decimal)))


D = {(3, 4): 6, (2, 4):8 }
print('\ndict d : \t',D)
print( isinstance( D[(3,4)] , tuple) )
print( isinstance( D[(3,4)] , int) )

def get_pos_of(i):
    if isinstance(D[i], int):
        i = D[i]
    return i

print('get_pos_of  :\t', get_pos_of( (2,4) ))



print('-------------- Correct way to handle lists with 0 elements -------------')
a=[7567,45,54645,5464]
if  [i for i in a if i < 3] :
    mx = max([i for i in a if i < 3])
else :
    print('asignam noi')


print('\n---------------- Assert and if raise statements -----------------')
# Use only one at a time :
def multiple_permutations(*args ) :
    ''' **©** Made by Bogdan Trif @ 2017-09-03, 12:15.
        Uses the formula Perm(total_elem_nr) / [ Perm(elem_1) *Perm(elem_2) * ...* Perm(elem_n) ]
    :param args:  the first arg is always the total number of elements, e.g. : for  the list [1, 1, 1, 1, 2, 2, 2 ,3, 3] = 9 elem ;
        The next elements will be in descending order the separate no of elem : 4 elem of '1' s , 3 elem of '2's , 2 elem of '3's
    :Explicit formula:      p = gmpy2.fac(9) // ( gmpy2.fac(4)*gmpy2.fac(3)*gmpy2.fac(2) )
    :return: int, Perm(total) / (Perm(elem_1) *Perm(elem_2) * ...* Perm(elem_n) )
    '''
    den = 1
    S=0          # the sum of all elements
    for i, j in enumerate(args) :
        # print(i,'    ', j,'     ' )
        if i == 0 :
            num = gmpy2.fac(j)
            N = j
        else :
            den *= gmpy2.fac(j)
            S += j
    # The both give the same outcome : assert and if raise are equivalent
    assert (N == S ) , "Total number of elements condition is not met !"

    if (N != S) :  raise ValueError ("Total number of elements condition is not met !")

    return (num // den)

print('\nMultiple_permutations of elements : \t' ,multiple_permutations(9,4,3,2) )