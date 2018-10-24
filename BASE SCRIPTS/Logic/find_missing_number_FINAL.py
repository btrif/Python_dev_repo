__author__ = 'trifb'        #2014-12-15     17:50
import random
import time

a = 100000000

t1 = time.time()

#Generating the array of consecutive numbers in the range defined by a
my_array = [i for i in range(a)]
             # the number of elements from my_array
#   For a > 65000 => Error. I guess that the append of the list no longer works properly.

#print(my_array, end='\n ')

missing_number = random.randint(0, a)
print('Generate a Random number: ', missing_number)
my_array.remove(missing_number)              # We remove the random generated number from my_array
print('The number of elements of the list is: ', len(my_array))             # Length of my array
print('the sum of the list is :',sum(my_array))                                 # sum

suma_completa = (a *(a-1)/2)
print('The complete sum of the consecutive numbers:',int(suma_completa),'\n')
print('And the missing number is:', int(suma_completa) - sum(my_array))

t2  = time.time()
print('\nCompleted in :', (t2-t1)*1000, 'ms')





