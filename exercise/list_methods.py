#  Created by Bogdan Trif on 29-06-2018 , 9:28 AM.
'''
http://interactivepython.org/runestone/static/pythonds/AlgorithmAnalysis/Lists.html

2.6. Lists
The designers of Python had many choices to make when they implemented the list data structure.
Each of these choices could have an impact on how fast list operations perform.
To help them make the right choices they looked at the ways that people would most commonly use
the list data structure and they optimized their implementation of a list so that the most common operations were very fast.
Of course they also tried to make the less common operations fast,
but when a tradeoff had to be made the performance of a less common operation
was often sacrificed in favor of the more common operation.

Two common operations are indexing and assigning to an index position.
Both of these operations take the same amount of time no matter how large the list becomes.
When an operation like this is independent of the size of the list they are O(1).

Another very common programming task is to grow a list.
There are two ways to create a longer list.
You can use the append method or the concatenation operator. The append method is O(1).
However, the concatenation operator is O(k) where k is the size of the list that is being concatenated.
This is important for you to know because it can help you make your own programs more efficient by choosing the right tool for the job.

Let’s look at four different ways we might generate a list of n numbers starting with 0.
First we’ll try a for loop and create the list by concatenation, then we’ll use append rather than concatenation.
Next, we’ll try creating the list using list comprehension and finally, and perhaps the most obvious way,
using the range function wrapped by a call to the list constructor.

Listing 3 shows the code for making our list four different ways.

Listing 3
'''

from timeit import Timer


def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [ i for i in range(1000) ]

def test4():
    l = list(range(1000))

'''
To capture the time it takes for each of our functions to execute we will use Python’s timeit module. 
The timeit module is designed to allow Python developers to make cross-platform timing measurements 
by running functions in a consistent environment and using timing mechanisms that are as similar as possible across operating systems.

To use timeit you create a Timer object whose parameters are two Python statements. 
The first parameter is a Python statement that you want to time; the second parameter is a statement 
that will run once to set up the test. 
The timeit module will then time how long it takes to execute the statement some number of times. 
By default timeit will try to run the statement one million times. 
When its done it returns the time as a floating point value representing the total number of seconds. 
However, since it executes the statement a million times you can read the result as the number of microseconds 
to execute the test one time. 
You can also pass timeit a named parameter called number that allows you to specify how many times the test statement is executed. 
The following session shows how long it takes to run each of our test functions 1000 times.
'''

t1 = Timer("test1()", "from __main__ import test1")
print("concat ", t1.timeit(number=1000), "  milliseconds")

t2 = Timer("test2()", "from __main__ import test2")
print("\nappend :   ", t2.timeit(number=1000), "    milliseconds")

t3 = Timer("test3()", "from __main__ import test3")
print("\ncomprehension :    ", t3.timeit(number=1000), "    milliseconds")

t4 = Timer("test4()", "from __main__ import test4")
print("\nlist range :   ", t4.timeit(number=1000), "    milliseconds")


print('\n------------------------------------')
'''
As a way of demonstrating this difference in performance let’s do another experiment using the timeit module. 
Our goal is to be able to verify the performance of the pop operation on a list of a known size when the program 
pops from the end of the list, and again when the program pops from the beginning of the list. 
We will also want to measure this time for lists of different sizes. 
What we would expect to see is that the time required to pop from the end of the list will stay constant even as the list grows in size, 
while the time to pop from the beginning of the list will continue to increase as the list grows.

Listing 4 shows one attempt to measure the difference between the two uses of pop. 
As you can see from this first example, popping from the end takes 0.0003 milliseconds, 
whereas popping from the beginning takes 4.82 milliseconds. For a list of two million elements this is a factor of 16,000.

There are a couple of things to notice about Listing 4. The first is the statement from __main__ import x. 
Although we did not define a function we do want to be able to use the list object x in our test. 
This approach allows us to time just the single pop statement and get the most accurate measure of the time for that single operation. 

Because the timer repeats 1000 times it is also important to point out that the list is decreasing in size by 1 each time through the loop. 
But since the initial list is two million elements in size we only reduce the overall size by 0.05%
'''
import timeit

popzero = timeit.Timer("x.pop(0)",                       "from __main__ import x")
popend = timeit.Timer("x.pop()",                       "from __main__ import x")

print("pop(0)   pop()")
for i in range(10**6, 10**7, 2*10**6):
    x = list(range(i))
    pt = popend.timeit(number=1000)
    x = list(range(i))
    pz = popzero.timeit(number=1000)
    print('i=' , i  , '   pop(0) : ' , round(pz,6) , ' ms;         pop() : ' , round(pt,6) ,' ms ' )


'''
Figure 3 shows the results of our experiment. 
You can see that as the list gets longer and longer the time it takes to pop(0) also increases while the time for pop stays very flat. 
This is exactly what we would expect to see for a O(n) and O(1) algorithm.

Some sources of error in our little experiment include the fact that there are other processes running on the computer 
as we measure that may slow down our code, so even though we try to minimize other things happening on the computer 
there is bound to be some variation in time. 
That is why the loop runs the test one thousand times in the first place to statistically gather enough information 
to make the measurement reliable.
'''