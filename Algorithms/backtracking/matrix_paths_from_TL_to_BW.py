#  Created by Bogdan Trif on 26-10-2017 , 11:17 AM.

# Count all possible paths from top left to bottom right of a mXn matrix
#
# The problem is to count all the possible paths from top left to bottom right of a mXn matrix with
# the constraints that from each cell you can either move only to right or down

# Python program to count all possible paths
# from top left to bottom right

# function to return count of possible paths
# to reach cell at row number m and column
# number n from the topmost leftmost
# cell (cell at 1, 1)
def numberOfPaths(m, n):
   # If either given row number is first
   # or given column number is first
   if(m == 1 or n == 1):
        return 1

   # If diagonal movements are allowed
   # then the last addition
   # is required.
   return  numberOfPaths(m-1, n) + numberOfPaths(m, n-1)

# Driver program to test above function
m = 3
n = 3
print(numberOfPaths(m, n))

# This code is contributed by Aditi Sharma


