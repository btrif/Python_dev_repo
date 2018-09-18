#  Created by Bogdan Trif on 17-07-2018 , 5:10 PM.

'''
            == OVERRIDING   ==
Defining a method in a subclass with the SAME NAME ,
SAME RETURN TYPE and SAME PARAMETERS that another one in the parent class is called overriding.

            == OVERLOADING  ==
Defining a method in a class with the same name,
same return type BUT DIFFERENT LIST OF PARAMETERS than another one in the same class is called overloading.


                    ===     Method overridding      ===
Is when you write the same function ( or method ) with same name, same return type  but having
 different number (list) of arguments

'''
print('-----------------    Function (Method) overridding  --------------------------')
def f(n):
    return n + 42

def f(n,m):
    return n + m + 42

print('f(3, 4) =  ' , f(3,4) ,'   works because we call the last function')
print('f(3) =  DOES NOT  work because we call the last function and we miss a second argument ')


'''
                                            ===     Method overloading      ===

In Python you can define a method in such a way that there are multiple ways to call it

Given a single method or function, we can specify the number of parameters ourself.

Depending on the function definition, it can be called with zero, one, two or more parameters.

This is known as method overloading.
Not all programming languages support method overloading, but Python does.

Example :
method( x)
method( x, y)
method( x, y, z)

    -   Method overloading example

We create a class with one method sayHello().
The first parameter of this method is set to None, this gives us the option to call it with or without a parameter.

An object is created based on the class, and we call its method using zero and one parameter.
'''
print('\n-----------------    Function (Method) OVERLOADING  --------------------------')

print('1.   Function example :')

def f(n, m=None):
    if m:
        return n + m +42
    else:
        return n + 42

print('f(3, 4) =  ' , f(3,4) ,'   works because we call the last function')
print('f(3) = ', f(3),'   works because we call the last function and we miss a second argument ')


print('\n2.   Class Method  :')

class Human:

    def sayHello(self, name=None):

        if name is not None:
            print( 'Hello ' + name)
        else:
            print('Hello ')

# Create instance
obj = Human()

# Call the method
print('# Call the method without parameter')
obj.sayHello()

# Call the method with a parameter
print('# Call the method with a parameter')
obj.sayHello('Guido')

'''
To clarify method overloading, we can now call the method sayHello() in two ways:

obj.sayHello()
obj.sayHello('Guido')
We created a method that can be called with fewer arguments than it is defined to allow.

We are not limited to two variables, your method could have more variables which are optional.
'''