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