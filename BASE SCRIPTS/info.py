#  Created by Bogdan Trif on 27-01-2018 , 7:05 PM.
'''
This chapter covers one of Python's strengths: introspection.
As you know, everything in Python is an object, and introspection is code looking
at other modules and functions in memory as objects, getting information about them, and manipulating them.

Along the way, you'll define functions with no name, call functions with arguments out of order, and reference functions
whose names you don't even know ahead of time.

Here is a complete, working Python program. You should understand a good deal about it just by looking at it.
The numbered lines illustrate concepts covered in Chapter 2, Your First Python Program.
Don't worry if the rest of the code looks intimidating; you'll learn all about it throughout this chapter.

'''

def info(object, spacing=10, collapse=1):
    """Print methods and doc strings.

    Takes module, class, list, dictionary, or string."""
    methodList = [method for method in dir(object) if callable(getattr(object, method))]
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    print("\n".join(["%s %s" %
                      (method.ljust(spacing),
                       processFunc(str(getattr(object, method).__doc__)))
                     for method in methodList]))

if __name__ == "__main__":
    print(info.__doc__)

    # EXAMPLE :
    li = []
    info(li)


