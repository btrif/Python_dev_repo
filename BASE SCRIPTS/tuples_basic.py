# an ordered sequence of elements, can mix element types
# immutable, cannot change element values
 # represented with parentheses
print('--------------TUPLES BASIC OPERATIONS ------------------')
te = ()
t = (2,"one",3, 'two')
print(t[0])
(2,"one",3) + (5,6)
print(t)                # Because is IMMUTABLE it remains the same

print(t[1:2] )                 #slice tuple, evaluates to ("one",)
print(t[1:3])                      #slice tuple, evaluates to ("one",3)
# t[1] = 4                    #gives error, can’t modify object

# Conveniently used to swap variable values because  x=y, y=x doesn't work
# (x, y) = (y, x)

def quotient_and_remainder(x, y):
    q = x//y
    r = x%y
    return(q, r)                        #return(q, r)

print(quotient_and_remainder(4,5))
