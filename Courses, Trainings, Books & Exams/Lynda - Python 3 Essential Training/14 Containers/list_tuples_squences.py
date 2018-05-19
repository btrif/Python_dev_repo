

#Create a tuple:  (immutable)
t = 1,2,3,4,5
print('Elements:',t,'---- Type:', type(t), '----Reference individual element:',t[0], '----Length:',len(t)) 

# Create a list:    (mutable)
l = [1,2,3,4,5]
print(l, type(l), len(l))

# Create a list from a range:
x = list(range(25,89,5))
print(x, type(x), x[4])
x[4] = 3432
print(x)

