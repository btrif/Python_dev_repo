#  Created by Bogdan Trif on 17-07-2018 , 6:15 PM.

'''
                                            ===     INNER CLASSES       ===

An inner class or nested class is a defined entirely within the body of another class.
If an object is created using a class, the object inside the root class can be used.
A class can have more than one inner classes, but in general inner classes are avoided.


                                            ==      Inner class example     ==
We create a class (Human) with one inner class (Head).
An instance is created that calls a method in the inner class:
'''

class Human:

    def __init__(self):
        self.name = 'Guido'
        self.head = self.Head()

    class Head:
        def talk(self):
            return 'talking...'

if __name__ == '__main__':
    guido = Human()
    print( guido.name)
    print( guido.head.talk())

'''
In the program above we have the inner class Head() which has its own method. 
An inner class can have both methods and variables. 
In this example the constructor of the class Human (__init__) creates a new head object.  
'''

print('                                     ==      Multiple inner classes      ==                                  ')
'''
                                            ==      Multiple inner classes      ==
You are by no means limited to the number of inner classes, for example this code will work too:
'''

class Human:

    def __init__(self):
        self.name = 'Guido'
        self.head = self.Head()
        self.brain = self.Brain()

    class Head:
        def talk(self):
            return 'talking...'

    class Brain:
        def think(self):
            return 'thinking...'

if __name__ == '__main__':
  guido = Human()
  print( guido.name)
  print( guido.head.talk())
  print( guido.brain.think())

'''
By using inner classes you can make your code even more object orientated. 
A single object can hold several sub objects.  We can use them to add more structure to our programs.
'''