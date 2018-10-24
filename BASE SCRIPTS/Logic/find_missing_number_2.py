__author__ = 'trifb'        #2014-12-15     17:50
from pylab import randint

my_array = []
a = 10000000             # the number of elements from my_array
#   For a > 65000 => Error. I guess that the append of the list no longer works properly.

for i in range(a):
    my_array.append(i)

#print(my_array, end='\n ')

missing_number = randint(a)
print('Generate a Random number: ', missing_number)
my_array.remove(missing_number)              # We remove the random generated number from my_array
print('The number of elements of the list is: ', len(my_array))             #Length of  my_array
print('the sum of the list is :',sum(my_array))                     #Sum

suma_completa = (a *(a-1)/2)
print('The complete sum of the consecutive numbers:',int(suma_completa),'\n')
print('And the missing number is:', int(suma_completa) - sum(my_array))