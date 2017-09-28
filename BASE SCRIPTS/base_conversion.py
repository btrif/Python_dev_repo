


# Converting an Integer to a String in Any Base

def toStr(n,base):
   '''Very elegant. Works Fine.
   :param n:
   :param base:
   :return:
   '''
   convertString = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefg"
   # print(len(convertString))
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

for i in range(2, 43) :
    print(toStr(43, i), end='  ')



print('\n--------------------- Binary Counter (Base 2 Counter ) -----------------')
# Binary counter
for x in range(16):
    print ( bin(x)[2:].zfill(4), end='   ')

print('\n--------------------- Base 3 Counter -----------------')

for i in range(0, 43) :
    print( toStr(i, 3), end='  ')



