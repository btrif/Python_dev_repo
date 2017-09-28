class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self): # Python 3: def __next__(self)
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


for c in Counter(3, 8):     print (c)

#########################################

class range:
      def __init__(self,a,b):
            self.a = a
            self.b = b
      def __iter__(self):
            i = self.a
            while i < self.b:
                  yield i
                  i+=1
for i in range(1,13): print(i, end=' ')



#########################################

def int2base(x,b,alphabet='0123456789abcdefghijklmnopqrstuvwxyz'):
    'convert an integer to its string representation in a given base'
    if b<2 or b>len(alphabet):
        if b==64: # assume base64 rather than raise error
            alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
        else:
            raise AssertionError("int2base base out of range")
    if isinstance(x,complex): # return a tuple
        return ( int2base(x.real,b,alphabet) , int2base(x.imag,b,alphabet) )
    if x<=0:
        if x==0:
            return alphabet[0]
        else:
            return  '-' + int2base(-x,b,alphabet)
    # else x is non-negative real
    rets=''
    while x>0:
        x,idx = divmod(x,b)
        rets = alphabet[idx] + rets
    return rets

print('\n',int2base(35,36))

###############################################

class baseRange:
    def __init__(self, low, high, base):
        digs = '0123456789abcdefghijklmnopqrstuvwxyz'
        self.current = low
        self.high = high
        self.base = base
    def __iter__(self):
        return self
    def __next__(self):  # Python 3 requires this to be __next__
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.int2base(self.current - 1, self.base)
    def int2base(x,b,alphabet='0123456789abcdefghijklmnopqrstuvwxyz'):
        'convert an integer to its string representation in a given base'
        if b<2 or b>len(alphabet):
            if b==64: # assume base64 rather than raise error
                alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
            else:
                raise AssertionError("int2base base out of range")
        if isinstance(x,complex): # return a tuple
            return ( int2base(x.real,b,alphabet) , int2base(x.imag,b,alphabet) )
        if x<=0:
            if x==0:
                return alphabet[0]
            else:
                return  '-' + int2base(-x,b,alphabet)
        # else x is non-negative real
        rets=''
        while x>0:
            x,idx = divmod(x,b)
            rets = alphabet[idx] + rets
        return rets

#for b in baseRange(2,89,7): print(i)

#################################
print('===='*20)
'''
There are four ways to build an iterative function:

1.  create a generator (uses the yield keyword)
2.  use a generator expression (genexp)
3.  create an iterator (defines __iter__ and __next__ (or next in Python 2.x))
4.  create a function that Python can iterate over on its own (defines __getitem__)
'''

# generator
def uc_gen(text):
    for char in text:
        yield char.upper()

# generator expression
def uc_genexp(text):
    return (char.upper() for char in text)

# iterator protocol
class uc_iter():
    def __init__(self, text):
        self.text = text
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        try:
            result = self.text[self.index].upper()
        except IndexError:
            raise StopIteration
        self.index += 1
        return result

# getitem method
class uc_getitem():
    def __init__(self, text):
        self.text = text
    def __getitem__(self, index):
        result = self.text[index].upper()
        return result

# To see all four methods in action :
for iterator in uc_gen, uc_genexp, uc_iter, uc_getitem:
    for ch in iterator('abcde'):
        print (ch, end=' ')
    print(iterator)


###############################

print('\n -----A PRIMITIVE CUSTOM BASE COUNTER, needs adjustments ----------------')
def makeCounter_iter(base):
    def isZero(lst): return lst == [0] * len(lst)

    def inc(num):
        if(len(num) > 1):
            rem = inc(num[:-1])
            if(isZero(rem)):
                if(num[-1] == base - 1):    rem.extend([0])
                else:                rem.extend([num[-1] + 1])
            else:    rem.extend([num[-1]])
            return rem
        else:
            new = [0]
            if(not num[0] == base - 1):    new[0] = num[0] + 1
            return new
    return inc


def makeCounter_rec(base):
    def incDigit(num, pos):
        new = num[:]
        if(num[pos] == base - 1):
            new[pos] = 0
            if(pos < len(num) - 1):    return incDigit(new, pos + 1)
        else:
            new[pos] = new[pos] + 1
        return new

    def inc(num): return incDigit(num, 0)
    return inc

base = 3
inc = makeCounter_iter(3)
n = [0, 0, 0]
print(len(n),n, type(n[0]))

for i in range( 0, base ** len(n)):
    n = inc(n)
    print (n, end = '   ')