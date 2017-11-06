#  Created by Bogdan Trif on 02-11-2017 , 12:19 PM.
# http://openbookproject.net/thinkcs/python/english3e/recursion.html

# 18.3. Processing recursive number lists
# To sum all the numbers in our recursive nested number list we need to traverse the list,
# visiting each of the elements within its nested structure, adding any numeric elements to our sum,
# and recursively repeating the summing process with any elements which are themselves sub-lists.
# Thanks to recursion, the Python code needed to sum the values of a nested number list is surprisingly short:


J = [ 1, 2, [11, 13], 8, [ [3, 5, [2, [4, 1, 1 ]] ,7 ], [ [[[[9,1]]]]  ] ] ]


def sum_nrs( J ):       # Made by Bogdan Trif @ 2017-11-02
    S=0
    for i in J :
        if type(i) == int :
            S+= i
        else :
            S += sum_nrs(i)

    return S


print( sum_nrs(J)    )


print('\n-------------------------------')

def r_sum(nested_num_list):
    tot = 0
    for element in nested_num_list:
        if type(element) == type([]):
            tot += r_sum(element)
        else:
            tot += element
    return tot

# The body of r_sum consists mainly of a for loop that traverses nested_num_list.
# If element is a numerical value (the else branch), it is simply added to tot.
# If element is a list, then r_sum is called again, with the element as an argument.
# The statement inside the function definition in which the function calls itself is known as the recursive call.
# The example above has a base case (on line 13) which does not lead to a recursive call:
# the case where the element is not a (sub-) list. Without a base case, you’ll have infinite recursion,
# and your program will not work.
# Recursion is truly one of the most beautiful and elegant tools in computer science.

print('\n ----------- find the maximum number in a nested list -------------------')
J = [ 1, 2, [11, 13], 8, [ [3, 5, [2, [4, 1, 1 ]] ,7 ], [ [[[[9,1], 87]]]  ] ] ]

def find_max(J, m):     # Made by Bogdan Trif @ 2017-11-02

    for i in J :
        if type(i) == int :
            if i > m :
                m = i
        else :
            m = find_max(i, m)

    return m

print(find_max(J, 0))


# A slightly more complicated problem is finding the largest value in our nested number list:
#Method II
def r_max(nxs):
    """
      Find the maximum in a recursive structure of lists
      within other lists.
      Precondition: No lists or sublists are empty.
    """
    largest = None
    first_time = True
    for e in nxs:
        if type(e) == type([]):
            val = r_max(e)
        else:
            val = e

        if first_time or val > largest:
            largest = val
            first_time = False

    return largest

# The added twist to this problem is finding a value for initializing largest.
# We can’t just use nxs[0], since that could be either a element or a list.
# To solve this problem (at every recursive call) we initialize a Boolean flag (at line 8).
# When we’ve found the value of interest, (at line 15) we check to see whether this is the initializing (first)
# value for largest, or a value that could potentially change largest.



print('\n----------- Example with recursive directories and files ------------------')
# The following program lists the contents of a directory and all its subdirectories.

import os

def get_dirlist(path):
    """
      Return a sorted list of all entries in path.
      This returns just the names, not the full path to the names.
    """
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist

def print_files(path, prefix = ""):
    """ Print recursive listing of contents of path """
    if prefix == "":  # Detect outermost call, print a heading
        print("Folder listing for", path)
        prefix = "| "

    dirlist = get_dirlist(path)
    for f in dirlist:
        print(prefix+f)                    # Print the line
        fullname = os.path.join(path, f)   # Turn name into full pathname
        if os.path.isdir(fullname):        # If a directory, recurse.
            print_files(fullname, prefix + "| ")