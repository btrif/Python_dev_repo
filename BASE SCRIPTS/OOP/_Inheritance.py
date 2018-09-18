#  Created by Bogdan Trif on 17-07-2018 , 5:15 PM.

'''
                                                 ===     Inheritance     ===
                                                    SUBCLASS, SUPERCLASS
Classes can inherit functionality of other classes.
If an object is created using a class that inherits from a superclass,
the object will contain the methods of both the class and the superclass.

The same holds true for variables of both the superclass and the class that inherits from the super class.

Python supports inheritance from multiple classes, unlike other popular programming languages.
'''

#   We define a basic class named User:
class User:
    name = ""

    def __init__(self, name):
        self.name = name

    def printName(self):
        print ("Name  = " + self.name)

'''
We then create another class called Programmer.
This looks very much like a standard class except than User is given in the parameters.
This means all functionality of the class User is accessible in the Programmer class.
'''

class Programmer(User):

    def __init__(self, name):
        self.name = name

    def doPython(self):
        print("Programming Python")

# This creates one instance called brian which outputs its given name.
brian = User("brian")
brian.printName()

# Now we use the inherited class, the Subclass Programmer :
diana = Programmer("Diana")
diana.printName()
diana.doPython()

'''
--  Brian is an instance of User and can only access the method printName. 
-- Diana is an instance of Programmer, a class with inheritance from User, 
and can access both the methods in Programmer and User.
'''

print('-----------------------------   ENCAPSULATION more detailed  ---------------------------')
'''
Syntax and Simple Inheritance Example :
We demonstrate inheritance in a very simple example. 
We create a Person class with the two attributes "firstname" and "lastname". 
This class has only one method, the Name method, essentially a getter, but we don't have an attribute name. 
This method is a further example for a "getter", which creates an output by creating it from more than one private attribute. 
Name returns the concatenation of the first name and the last name of a person, separated by a space. 
It goes without saying that a useful person class would have additional attributes and further methods. 

This chapter of our tutorial is about inheritance, so we need a class, which inherits from Person. 
So far employees are Persons in companies, even though they may not be treated as such in some firms. 
If we created an Employee class without inheriting from Person, 
we would have to define all the attributes and methods in the Employee class again. 
This means we would create a design and maybe even a data redundancy. 
With this in mind, we have to let Employee inherit from Person. 

The syntax for a subclass definition looks like this:

class DerivedClassName(BaseClassName):
    pass
    
Of course, usually we will have an indented block with the class attributes and methods instead of merely a pass statement. 
The name BaseClassName must be defined in a scope containing the derived class definition. 
With all this said, we can implement our Person and Employee class:
 
 class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def Name(self):
        return self.firstname + " " + self.lastname

class Employee(Person):

    def __init__(self, first, last, staffnum):
        Person.__init__(self, first, last )
        self.staffnumber = staffnum

    def GetEmployee(self):
        return self.Name() + ", " +  self.staffnumber

x = Person("Marge", "Simpson")
y = Employee("Homer", "Simpson", "1007")

print(x.Name())
print(y.GetEmployee())

Our program returns the following output: 

$ python3 person.py 
Marge Simpson
Homer Simpson, 1007

The __init__ method of our Employee class explicitly invokes the __init__method of the Person class. 
We could have used super instead. super().__init__(first, last) is automatically replaced by a call to the superclasses method, 
in this case __init__:

    def __init__(self, first, last, staffnum):
        super().__init__(first, last)
        self.staffnumber = staffnum
        
Please note that we used super()) without arguments. This is only possible in Python3. 
We could have written "super(Employee, self).__init__(first, last, age)" which still works in Python3 and is compatible with Python2.
 

                    ==  Overloading and Overriding  ==

Instead of using the methods "Name" and "GetEmployee" in our previous example, 
it might have been better to put this functionality into the "__str__" method. In doing so, 
we gain a lot, especially a leaner design. 
We have a string casting for our classes and we can simply print out instances. 

Let's start with a __str__ method in Person:
'''

class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def __str__(self):
        return self.firstname + " " + self.lastname

class Employee(Person):

    def __init__(self, first, last, staffnum):
        super().__init__(first, last)
        self.staffnumber = staffnum


x = Person("Marge", "Simpson")
y = Employee("Homer", "Simpson", "1007")

print('x : ', x)
print('y : ', y)

'''
The output looks like this:
$ python3 person2.py 
Marge Simpson
Homer Simpson

First of all, we can see that if we print an instance of the Employee class, the __str__ method of Person is used. 
This is due to inheritance. 
The only problem we have now is the fact that the output of "print(y)" is not the same as the "print(y.GetEmployee())". 
This means that our Employee class needs its own __str__ method. 
We could write it like this:

    def __str__(self):
        return self.firstname + " " + self.lastname + ", " +  self.staffnumber
        
But it is a lot better to use the __str__ method of Person inside of the new definition. 
This way, we can make sure that the output of the Employee __str__method will automatically change, 
if the __str__ method from the superclass Person changes. 
We could, for example, add a new attribute age in Person:
'''
print('------------------------     Overloading and Overriding      -------------------')

class Person:

    def __init__(self, first, last, age):
        self.firstname = first
        self.lastname = last
        self.age = age

    def __str__(self):
        return self.firstname + " " + self.lastname + ", " + str(self.age)

class Employee(Person):

    def __init__(self, first, last, age, staffnum):
        super().__init__(first, last, age)
        self.staffnumber = staffnum

    def __str__(self):
        return super().__str__() + ", " +  self.staffnumber


x = Person("Marge", "Simpson", 36)
y = Employee("Homer", "Simpson", 28, "1007")

print('x : ', x)
print('y : ', y)


'''
We have overridden the method __str__ from Person in Employee. 
By the way, we have overridden __init__ also. 
Method overriding is an object-oriented programming feature that allows a subclass to provide a different implementation 
of a method that is already defined by its superclass or by one of its superclasses. 
The implementation in the subclass overrides the implementation of the superclass by providing a method 
with the same name, same parameters or signature, and same return type as the method of the parent class.

Overwriting is not a different concept but usually a term wrongly used for overriding! 

In the context of object-oriented programming, you might have heard about "overloading" as well. 
Overloading is the ability to define the same method, with the same name but with a different number of arguments and types. 
It's the ability of one function to perform different tasks, depending on the number of parameters or the types of the parameters. 

Let's look first at the case, in which we have the same number of parameters but different types for the parameters. 
When we define a function in Python, we don't have to and we can't declare the types of the parameters. 
So if we define the function "successor" in the following example, we implicitly define a family of function, i.e. a function, 
which can work on integer values, one which can cope with float values and so. 
Of course, there are types which will lead to an error if used
'''