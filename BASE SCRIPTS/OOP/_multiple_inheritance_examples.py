#  Created by Bogdan Trif on 22-08-2018 , 9:04 PM.
# https://stackoverflow.com/questions/3277367/how-does-pythons-super-work-with-multiple-inheritance

print('---------------          EXAMPLE  1           -----------')

class First(object):
    def __init__(self):
        super(First, self).__init__()
        print("first")

class Second(object):
    def __init__(self):
        super(Second, self).__init__()
        print("second")

class Third(First, Second):
    def __init__(self):
        super(Third, self).__init__()
        print("third")


Third()

print('---------------          EXAMPLE 2           -----------')

class A(object):
    def __init__(self, a, *args, **kwargs):
        print("A", a)

class B(A):
    def __init__(self, b, *args, **kwargs):
        super(B, self).__init__(*args, **kwargs)
        print("B", b)

class A1(A):
    def __init__(self, a1, *args, **kwargs):
        super(A1, self).__init__(*args, **kwargs)
        print("A1", a1)

class B1(A1, B):
    def __init__(self, b1, *args, **kwargs):
        super(B1, self).__init__(*args, **kwargs)
        print("B1", b1)


B1(a1=6, b1=5, b="hello", a=None)


print('---------------          EXAMPLE 3           -----------')

class Foo:
    def __init__(self):
        self.foo = 'foo'

class Bar:
    def __init__(self, bar):
        self.bar = bar

class FooBar(Foo, Bar):
    def __init__(self, bar='bar'):
#         Foo.__init__(self)  # explicit calls without super
#         Bar.__init__(self, bar)

        # To get the same results with `super`, you'd have to do this:
          super().__init__()
          super(Foo, self).__init__(bar)
        # Which is obviously much less intuitive.

X = FooBar('higgs')
X.bar

print('---------------          EXAMPLE  4           -----------')

class A(object):
    def __init__(self, URL, **kwargs ) :
        super().__init__( **kwargs )
        self.URL = URL
        self.CUSTOMERS = self.get_Content()

    def get_Content( self ) :
        # print('class A method return from URL ' + str(self.URL))
        return 'class A which gets the content from the URL : ' +str(self.URL)

class B( object ) :
    def __init__(self, file, **kwargs ):
        super().__init__( **kwargs)
        self.file = file
        self.valid_Customers = self.read_file()

    def read_file( self ) :
        # print('the file "' +str(self.file) +'" contains the following data :')
        return ['customer'+str(i) for i in range(5)]

class C(  A , B  ):
    def __init__( self, URL, file ) :
        # super().__init__()
        super().__init__( URL=URL, file=file )

        print(self.URL)
        print( self.CUSTOMERS )
        print( self.file )
        print(self.valid_Customers)

# X = A('http://something.com')
# Y = B('some_file.txt')
# Y.valid_Customers
Z = C( 'http://something.com', 'some_file.txt' )
# Z = C( 'http://something.com'  )



print('---------------          EXAMPLE  5          -----------')

class CoopFoo:
    def __init__(self, foo, **kwargs):
        super().__init__(**kwargs)
        self.foo = foo

class CoopBar:
    def __init__(self, bar, **kwargs):
        super().__init__( **kwargs)
        self.bar = bar

class CoopFooBar(CoopFoo, CoopBar):
    def __init__(self, foo, bar):
        super().__init__(foo=foo, bar=bar)  # pass all arguments on as keyword
                                   # arguments to avoid problems with
                                   # positional arguments and the order
                                   # of the parent classes

CFB = CoopFooBar(34,'geometry')
print(CFB.foo)
print(CFB.bar)

