import bisect, pickle


print(dir(bisect))

########################
# The bisect() function can be useful for numeric table lookups.
# This example uses bisect() to look up a letter grade for an exam score (say)
# based on a set of ordered numeric breakpoints: 90 and up is an ‘A’, 80 to 89 is a ‘B’, and so on:

def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
        i = bisect.bisect(breakpoints, score)
        return grades[i]

print( [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]] )


#################################

# The above bisect() functions are useful for finding insertion points but
# can be tricky or awkward to use for common searching tasks.
# The following five functions show how to transform them into the standard lookups for sorted lists:



def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

def find_lt(a, x):
    'Find rightmost value less than x'
    i = bisect.bisect_left(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect.bisect_right(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bisect.bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError

def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i = bisect.bisect_left(a, x)
    if i != len(a):
        return a[i]
    raise ValueError


print('\n-------------------pickle module---------------------\n')

print(dir(pickle))


 # Save a dictionary into a pickle file.
import pickle

favorite_color = { "lion": "yellow", "kitty": "red" }
pickle.dump( favorite_color, open( "save.txt", "wb" ) )

# Load the dictionary back from the pickle file.

favorite = pickle.load( open( "save.txt", "rb" ) )
print(favorite,'\nWOW ! That was nice !')