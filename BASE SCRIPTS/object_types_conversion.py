print('----------'*13)
print('........................Function which transforms a string into a list:   ....................')
def string_to_list(strng):
   if (type(strng) == str):
      lst = list(strng)
      print(lst)
      print('The type of   ',lst, 'is :  ',type(lst))
      return lst
   else: print('Not a string type !')

string_to_list('1218565')

print('----------'*13)
print('........................Function which transforms a list into a string:   ....................')

def list_to_string(lst):
   if ( type(lst) == list ):
      strng = ''.join(lst)
      print(strng)
      print('Type of  ',strng,' is:  ',type(strng))
      return strng
   else: print('Not a list (array) type !')

list_to_string(['4','5','7','9','1','8'])

print('----------'*13)
print('........................Function which transforms a tuple into a string:   ....................')


def tuple_to_string(tup):
   if ( type(tup) == tuple ):
      strng = ''.join(map(str, (tup)))
      print(strng)
      print('Type of  ',strng,' is:  ',type(strng))
      return strng
   else: print('Not a tuple type !')

print('........................Function which transforms a tuple into a list:   ....................')

def tuple_to_list(tup):
   if ( type(tup) == tuple ):
      lst = [str(i) for i in tup]
      print(lst)
      print('Type of  ',lst,' is:  ',type(lst))
      return lst
   else: print('Not a tuple type !')


tup = ('a', 'b', 'c', 'd', 'g', 'x', 'r', 'e'); print(tup, type(tup))
tuple_to_string(tup)

bic=(9, 8, 1); print(bic ,type(bic))
tuple_to_string(bic)

st=('4','3',3,2,2) ; print(type(st),st)
tuple_to_list((st))


# Simple command for TUPLE TO STRING Conversion :
mystring = ' '.join(map(str, (34.2424, -64.2344, 76.3534, 45.2344)))
print(mystring, type(mystring))

# Simple TUPLE TO LIST CONVERSION :
just_tuple=(34.2424, -64.2344, 76.3534, 45.2344);  print(type(just_tuple), just_tuple)
A = [str(i) for i in (34.2424, -64.2344, 76.3534, 45.2344)] ;
print(type(A), A)

# String going backwards, REVERSE STRING:
#So, in a nutshell, if :
a = '12345'
print(a[::2])               # becomes 135
print(a[::-1])              #becomes 54321
print(a[::-2])              #becomes 531

print('-----'*20)
# Count unique items in a list :
words = ['a', 'b', 'c', 'a']
unique_words = set(words)                # == set(['a', 'b', 'c'])
unique_word_count = len(unique_words)    # == 3
print('Unique words :   ',len(unique_words))

print('-----'*20)
b = [a for a in range(11)] ; print('The sum of a list of integers :   ',sum(b))
