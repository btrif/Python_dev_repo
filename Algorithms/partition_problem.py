import time

### MEHOD I
# Determine a subset which has THE SUM  balanced with a second subset

def subsetsum(array, num):

    if num == 0 or num < 1:
        return None
    elif len(array) == 0:
        return None
    else:
        if array[0] == num:
            return [array[0]]
        else:
            with_v = subsetsum(array[1:],(num - array[0]))
            if with_v:
                return [array[0]] + with_v
            else:
                return subsetsum(array[1:],num)

P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181]
print( sum(P))
s1 = subsetsum(P, sum(P)//2)
print('First Subset : \t', s1)
s1 = set(s1)
s2 = set(P)-s1
print('Second Subset : \t', s2)



##### PROBLEM II
# Given a set of non-negative integers, and a value sum, determine if there is a subset
# of the given set with sum equal to given sum.

# // Returns true if there is a subset of set[] with sum equal to given sum
def  isSubsetSum(sett , n,  suma ) :        ## ( ͡° ͜ʖ ͡°)  FASTEST  ( ͡° ͜ʖ ͡°)  ### !! FIRST FASTEST
                                                                    ## !!!!!!!! ALGORITHM FAR MORE EFFICIENT !!!!!!
   # // Base Cases
    if (suma == 0) :
        return True
    if (n == 0 and suma != 0 ):
        return False;

   # // If last element is greater than sum, then ignore it
    if (sett[n-1] > suma) :
        return isSubsetSum(sett, n-1, suma)

   # /* else, check if sum can be obtained by any of the following
   #    (a) including the last element
   #    (b) excluding the last element   */
   #  return isSubsetSum(sett, n-1, suma)
    return isSubsetSum(sett, n-1, suma-sett[n-1] )


def main() :

  sett = [3, 34, 4, 12, 5, 2]
  suma = 9
  n = len(sett)//sett[0]
  if (isSubsetSum(sett, n, suma) == True) :
        print("Found a subset with given sum")
  else:
        print("No subset with given sum")
  return 0

main()



# # #################### #####################

# test_array, test_nr = [1, 2, 3, 6, 9, 13, 18, 23, 26, 39, 46, 69, 78, 117, 138, 207, 234, 299, 414, 598, 897, 1794, 2691], 4599
test_array, test_nr = [1, 2, 3, 6, 9, 13, 18, 23, 26, 39, 46, 69, 78, 117, 138, 207, 234, 299, 414, 598, 897, 1794, 2691], 7913

print('\n--------------- 1 ------------------')
t1  = time.time()

print( subsetsum(test_array, test_nr) )



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

# # #################### #####################

print('\n--------------- 2 --- SECOND ALGORITHM MUCH FASTER ---------------')
t1  = time.time()

print( isSubsetSum(test_array, len(test_array) ,test_nr) )


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


