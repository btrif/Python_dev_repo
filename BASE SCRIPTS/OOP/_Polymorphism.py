#  Created by Bogdan Trif on 17-07-2018 , 5:21 PM.
'''
                                                ===         Polymorphism            ===
                                                    OVERRIDING & OVERLOADING
Sometimes an object comes in many types or forms.
If we have a button, there are many different draw outputs (round button, check button, square button, button with image)
but they do share the same logic: onClick().
We access them using the same method .
This idea is called Polymorphism.

Polymorphism is based on the greek words Poly (many) and morphism (forms).
We will create a structure that can take or use many forms of objects.

== OVERRIDING   ==
Defining a method in a subclass with the SAME NAME ,
SAME RETURN TYPE and SAME PARAMETERS that another one in the parent class is called overriding.

== OVERLOADING  ==
Defining a method in a class with the same name,
same return type BUT DIFFERENT LIST OF PARAMETERS than another one in the same class is called overloading.

'''

'''
                        ==  Polymorphism with a function:   ==
                        
We create two classes:  Bear and Dog, both  can make a distinct sound.
'''

class Bear(object):
    def sound(self):
        print ("Groarrr")

class Dog(object):
    def sound(self):
        print( "Woof woof!")

def makeSound(animalType):
    animalType.sound()

bearObj = Bear()
dogObj = Dog()

# We then make two instances and call their action using the same method.
makeSound(bearObj)
makeSound(dogObj)

'''
                                    ==      Polymorphism with abstract class (most commonly used)   ==

If you create an editor you may not know in advance what type of documents a user will open (pdf format or word format?).  
Wouldn’t it be great to access them like this,  instead of having 20 types for every document?

Polymorphism visual. Abstract structure is defined in Document class.

for document in documents:
    print( document.name + ': ' + document.show() )
    
To do so, we create an abstract class called document.  
This class does not have any implementation but defines the structure (in form of functions) that all forms must have.  

If we define the function show()  then both the PdfDocument and WordDocument must have the show() function. 
 Full code:
'''
class Document:
    def __init__(self, name):
        self.name = name

    def show(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Pdf(Document):
    def show(self):
        return 'Show pdf contents!'

class Word(Document):
    def show(self):
        return 'Show word contents!'

# Now we instantiate two Pdf class objects and one Word class object :
documents = [ Pdf('Raspberry Pi - Getting Started'),              Pdf('Learn Python'),   Word('3 ways to be happy')]

for document in documents:
    print('doc name : ', document.name + '     -     ' + document.show() )

# We have an abstract access point (document) to many types of objects (pdf,word) that follow the same structure.

print('\n                       ===     Polymorphism example       ===                              ')
'''

                                                        ===     Polymorphism example       ===        

Another example would be to have an abstract class Car which holds the structure  drive() and stop().  
We define two objects Sportscar and Truck, both are a form of Car. 

In pseudo code what we will do is:

class Car:
    def drive abstract, no implementation.
    def stop abstract, no implementation.
 
class Sportscar(Car):
    def drive: implementation of sportscar
    def stop: implementation of sportscar
 
class Truck(Car):
    def drive: implementation of truck
    def stop: implementation of truck

Then we can access any type of car and  call the functionality without taking further into account if the form is Sportscar or Truck.  
Full code:
'''

class Car:
    def __init__(self, name):
        self.name = name

    def drive(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def stop(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Sportscar(Car):
    def drive(self):
        return 'Sportscar driving!'

    def stop(self):
        return 'Sportscar braking!'

class Truck(Car):
    def drive(self):
        return 'Truck driving slowly because heavily loaded.'

    def stop(self):
        return 'Truck braking!'

# We instantiate the classes into objects :
cars = [ Truck('Bananatruck'),         Truck('Orangetruck'),         Sportscar('Z3') ]

for car in cars:
    print( car.name + '     :        ' + car.drive() )