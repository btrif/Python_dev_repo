


# Converting an Integer to a String in Any Base

def toStr(n, base ):        # Recursion Solution
   '''Very elegant. Works Fine. 2017-10-16 - Has problems for huge numbers > 500 digits. Because of the
   sys.getrecursionlimit() . I tried o increase it to sys.setrecursionlimit(10000000) and
   when dealing with 2000 digit numbers fails again .

   :param n:, int, number to transform in the other base
   :param base:int, base
   :return: int, the number n transformed in the new base                      '''

   convertString = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefg"
   # print(len(convertString))
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]



def baseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])


def baseconvert(n, base):
    """convert positive decimal integer n to equivalent in another base (2-36)"""

    digits = "0123456789abcdefghijklmnopqrstuvwxyz"

    try:
        n = int(n)
        base = int(base)
    except:
        return ""

    if n <= 0 or base <= 2 or base >= 36:
        return ""

    s = ""
    while 1:
        r = n % base
        s = digits[r] + s
        n = n // base
        if n == 0:
            break

    return s


print('\n-------------------- Converts from any base to decimal -----------------')

print('\n', int('2D', 14) )         # From base 14 in Decimal


print('\n--------------------- Binary Counter (Base 2 Counter ) -----------------')
# Binary counter
for x in range(16):
    print ( bin(x)[2:].zfill(4), end='   ')

print('\n--------------------- Base 3 Counter -----------------')

for i in range(0, 43) :
    print( toStr(i, 3), end='  ')




