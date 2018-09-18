#  Created by Bogdan Trif on 17-07-2018 , 6:21 PM.
# https://pythonspot.com/factory-method/

'''
                                                ===     Factory method      ===

We may not always know what kind of objects we want to create in advance.
Some objects can be created only at execution time after a user requests so.

Examples when you may use a factory method:

A user may click on a certain button that creates an object.
A user may create several new documents of different types.
If a user starts a web browser, the browser does not know in advance how many tabs (where every tab is an object) will be opened.

        =   Factory method pattern
To deal with this we can use the factory method pattern.
The idea is to have one function, the factory, that takes an input string and outputs an object.

obj = Car.factory("Racecar")
obj.drive()

    =   Key fact: a factory method returns (new) objects.

The type of object depends on the type of input string you specify.
This technique could make your program more easily extensible also.
A new programmer could easily add functionality by adding a new string and class,
without having to read all of the source code.

                                            ==      Factory method example      ==
The example below demonstrates a factory method.
The factory method (named factory) returns a new object of either type depending on the input.

'''

class Car(object):

    def factory(type):
        if type == "Racecar":
            return Racecar()
        if type == "Van":
            return Van()
        assert 0, "Bad car creation: " + type

    factory = staticmethod(factory)

class Racecar(Car):
    def drive(self):
        print("Racecar driving.")

class Van(Car):
    def drive(self):
        print("Van driving.")

# Create object using factory.
obj = Car.factory("Racecar")
obj.drive()