#  Created by Bogdan Trif on 10-07-2018 , 4:42 PM.
# http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementingaDequeinPython.html

'''
As we have done in previous sections, we will create a new class for the implementation of the abstract data type deque.
Again, the Python list will provide a very nice set of methods upon which to build the details of the deque.
Our implementation (Listing 1) will assume that the rear of the deque is at position 0 in the list.
'''


class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


print('\n----------------------       APPLICATIONS  --------------------------')
print('----------------------       3.18. Palindrome-Checker  --------------------------')

'''
3.18. Palindrome-Checker
An interesting problem that can be easily solved using the deque data structure is the classic palindrome problem. 
A palindrome is a string that reads the same forward and backward, for example, radar, toot, and madam. 
We would like to construct an algorithm to input a string of characters and check whether it is a palindrome.

The solution to this problem will use a deque to store the characters of the string. 
We will process the string from left to right and add each character to the rear of the deque. 
At this point, the deque will be acting very much like an ordinary queue. 
However, we can now make use of the dual functionality of the deque. 
The front of the deque will hold the first character of the string and the rear of the deque will hold the last character (see Figure 2).
'''

def palchecker(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual :
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual

print(palchecker("lsdkjfskf"))
print(palchecker("radar"))