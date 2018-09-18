#  Created by Bogdan Trif on 04-06-2018 , 10:26 PM.

# https://realpython.com/python-thinking-recursively/


houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]

def deliver_presents_iteratively():
    for house in houses:
        print("Delivering presents to", house)


deliver_presents_iteratively()

print('\n-------------      Recursion       ----------------')

'''
But I feel for Santa. At his age, he shouldn’t have to deliver all the presents by himself. 
I propose an algorithm with which he can divide the work of delivering presents among his elves:

Appoint an elf and give all the work to him
Assign titles and responsibilities to the elves based on the number of houses for which they are responsible:
> 1 He is a manager and can appoint two elves and divide his work among them
= 1 He is a worker and has to deliver the presents to the house assigned to him

This is the typical structure of a recursive algorithm. If the current problem represents a simple case, solve it. 
If not, divide it into subproblems and apply the same strategy to them.

The algorithm for recursive present delivery implemented in Python:

'''

houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house", "Bogdan's house"]

# Each function call represents an elf doing his work
def deliver_presents_recursively(houses):

    # Worker elf doing his work
    if len(houses) == 1 :
        print("Delivering presents to", houses[0]  )

     # Manager elf doing his work
    else :
        left_half = houses[ : len(houses)//2 ]
        right_half = houses[ len(houses)//2 : ]


        # Divides his work among two elves
        deliver_presents_recursively( left_half )
        deliver_presents_recursively( right_half )


deliver_presents_recursively( houses )

print('\n--------------------------       Maintaining State          ----------------------------')
'''
Maintaining State
When dealing with recursive functions, keep in mind that each recursive call has its own execution context, 
so to maintain state during recursion you have to either:

Thread the state through each recursive call so that the current state is part of the current call’s execution context
Keep the state in global scope
A demonstration should make things clearer. Let’s calculate 1 + 2 + 3 ⋅⋅⋅⋅ + 10 using recursion. 
The state that we have to maintain is (current number we are adding, accumulated sum till now).

Here’s how you do that by threading it through each recursive call (i.e. passing the updated current state to each recursive call as arguments):
'''

def sum_recursive(current_number, accumulated_sum):
    # Base case
    # Return the final state
    if current_number == 11:
        return accumulated_sum

    # Recursive case
    # Thread the state through the recursive call
    else :
        return sum_recursive( current_number+1   , current_number + accumulated_sum  )


print('sum_recursive : ', sum_recursive( 1 ,0 ))

print('\n-------------------------    maintain the state by keeping it in global scope:          -------------------------')
# Here’s how you maintain the state by keeping it in global scope:
# Global mutable state
current_number = 1
accumulated_sum = 0


def sum_recursive_2():
    global current_number
    global accumulated_sum
    # Base case
    if current_number == 11:
        return accumulated_sum
    # Recursive case
    else:
        accumulated_sum = accumulated_sum + current_number
        current_number = current_number + 1
        return sum_recursive_2()


print('sum_recursive_2 : ', sum_recursive_2(  ))



print('\n---------------------      1.7.3   Printing in Recursive Functions           ----------------------')
'''
The computational process evolved by a recursive function can often be visualized using calls to print. 
As an example, we will implement a function cascade that prints all prefixes of a number from largest to smallest to largest.
'''

def cascade(n):
        """Print a cascade of prefixes of n."""
        if n < 10:
            print(n)
        else:
            print(n)
            cascade(n//10)
            print(n)

cascade(20135)

'''
In this recursive function, the base case is a single-digit number, which is printed. 
Otherwise, a recursive call is placed between two calls to print.

It is not a rigid requirement that base cases be expressed before recursive calls. 
In fact, this function can be expressed more compactly by observing that print(n) is repeated in both clauses of the conditional statement, 
and therefore can precede it.
'''

def cascade(n):
        """Print a cascade of prefixes of n."""
        print(n)
        if n >= 10:
            cascade(n//10)
            print(n)




print('\n----------------- 1.7.2   Mutual Recursion ------------------------')
'''
When a recursive procedure is divided among two functions that call each other, the functions are said to be mutually recursive. 
As an example, consider the following definition of even and odd for non-negative integers:

a number is even if it is one more than an odd number
a number is odd if it is one more than an even number
0 is even
Using this definition, we can implement mutually recursive functions to determine whether a number is even or odd:
'''

def is_even(n):
    if n == 0:
        return True
    else:
        return is_odd(n-1)

def is_odd(n):
    if n == 0:
        return False
    else:
        return is_even(n-1)

result = is_even(4)

'''
Mutually recursive functions can be turned into a single recursive function by breaking the abstraction boundary 
between the two functions. In this example, the body of is_odd can be incorporated into that of is_even, 
making sure to replace n with n-1 in the body of is_odd to reflect the argument passed into it:
'''
def is_even(n):
        if n == 0:
            return True
        else:
            if (n-1) == 0:
                return False
            else:
                return is_even((n-1)-1)


'''
As such, mutual recursion is no more mysterious or powerful than simple recursion, 
and it provides a mechanism for maintaining abstraction within a complicated recursive program.
'''


print('\n----------------- Mutual recursion ------------------------')
'''
As another example of mutual recursion, consider a two-player game in which there are n initial pebbles on a table. 
The players take turns, removing either one or two pebbles from the table, and the player who removes the final pebble wins. 
Suppose that Alice and Bob play this game, each using a simple strategy:

= Alice always removes a single pebble
 = Bob removes two pebbles if an even number of pebbles is on the table, and one otherwise

Given n initial pebbles and Alice starting, who wins the game?

A natural decomposition of this problem is to encapsulate each strategy in its own function. 
This allows us to modify one strategy without affecting the other, maintaining the abstraction barrier between the two. 
In order to incorporate the turn-by-turn nature of the game, these two functions call each other at the end of each turn.
'''

def play_alice(n):
        if n == 0:
            print("Bob wins!")
        else:
            play_bob(n-1)

def play_bob(n):
        if n == 0:
            print("Alice wins!")
        elif is_even(n):
            play_alice(n-2)
        else:
            play_alice(n-1)

play_alice(20)

''' In play_bob, we see that multiple recursive calls may appear in the body of a function. 
However, in this example, each call to play_bob calls play_alice at most once. 
In the next section, we consider what happens when a single function call makes multiple direct recursive calls.
'''


print('\n------------------ 1.7.5   Example: Partitions     ------------------')
'''
The number of partitions of a positive integer n, using parts up to size m, 
is the number of ways in which n can be expressed as the sum of positive integer parts up to m in increasing order. 
For example, the number of partitions of 6 using parts up to 4 is 9.

6 = 2 + 4
6 = 1 + 1 + 4
6 = 3 + 3
6 = 1 + 2 + 3
6 = 1 + 1 + 1 + 3
6 = 2 + 2 + 2
6 = 1 + 1 + 2 + 2
6 = 1 + 1 + 1 + 1 + 2
6 = 1 + 1 + 1 + 1 + 1 + 1

We will define a function count_partitions(n, m) that returns the number of different partitions of n using parts up to m. 
This function has a simple solution as a tree-recursive function, based on the following observation:

The number of ways to partition n using integers up to m equals

1.  the number of ways to partition n-m using integers up to m, and
2.  the number of ways to partition n using integers up to m-1.

To see why this is true, observe that all the ways of partitioning n can be divided into two groups: 
those that include at least one m and those that do not. 
Moreover, each partition in the first group is a partition of n-m, followed by m added at the end. 

In the example above, the first two partitions contain 4, and the rest do not.

Therefore, we can recursively reduce the problem of partitioning n using integers up to m into two simpler problems: 
(1) partition a smaller number n-m, and 
(2) partition with smaller components up to m-1.

To complete the implementation, we need to specify the following base cases:

1.  There is one way to partition 0: include no parts.
2.  There are 0 ways to partition a negative n.
3.  There are 0 ways to partition any n greater than 0 using parts of size 0 or less.
'''

def count_partitions( n, m) :
    '''Count the ways to partition n using parts up to m.'''

    if n == 0 :
        return 1
    elif n < 0 :
        return 0
    elif m== 0:
        return 0
    else :
        return count_partitions( n-m, m ) + count_partitions(n, m-1  )


print('count_partitions : ', count_partitions( 6 , 4  ))
'''
We can think of a tree-recursive function as exploring different possibilities. 
In this case, we explore the possibility that we use a part of size m and the possibility that we do not. 
The first and second recursive calls correspond to these possibilities.

Implementing this function without recursion would be substantially more involved.

'''