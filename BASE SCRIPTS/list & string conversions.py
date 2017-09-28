
print('\n------------------     Transform a string into a list  : ------------------------------')
my_string='3567'                                        #Original string
print(my_string,'    Type:   ',type(my_string))

my_list=list(my_string)                                                         # Transform string into a list
print(my_list,'    Type:   ',type(my_list))

s = 'pining for the fjords'
t = s.split()
print (t)




print('\n-----------   Transform back the list into a string   ---------------')
string2=''.join(my_list)                                                        # Transform back the list into a string
print(string2,'    Type:   ',type(string2))



print('----------'*13)

list1 = ['1', '2', '3']
str1 = ''.join(list1); print(str1,'     Type:    ',type(str1))

# Or if the list is of integers, convert the elements before joining them.
print('\n------------  if the LIST is of INTEGERS, convert the elements before joining them : -------------------- ')
list1 = [1, 2, 3]
str1 = ''.join(str(e) for e in list1); print(str1,'     Type:    ',type(str1))


print('\n ----------Work also for TUPLES with INTEGERS: ----------------------------')
tp = (0,1,2,3,4,5,6,7,8,9)
str1 = ''.join(str(i) for i in list(tp)); print(str1,'     Type:    ',type(str1))

print('\n-------------------------   JOIN a List of integers -------------------------')

L = [1,2,3]
print(L,end='                   ')
print(''.join(str(x) for x in L))

print('........................Function which transforms a string into a list:   ....................')
def string_to_list(strng):
   if (type(strng) == str):
      lst = list(strng)
      print(lst, type(lst))
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