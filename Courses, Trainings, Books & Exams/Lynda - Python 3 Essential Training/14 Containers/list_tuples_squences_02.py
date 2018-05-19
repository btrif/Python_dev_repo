#Create a tuple:  (immutable)
t = 1,2,3,4,5
print('Elements:',t,'---- Type:', type(t), '----Reference individual element:',t[0], '----Length:',len(t))
print(t.count(11))


# Create a list:    (mutable)
l = [1,2,3,4,5]
print(l, type(l), len(l))
print(l.count(4))

# Create a list from a range:
x = list(range(25,89,5))
print(x, type(x), x[4])

x[4] = 595959           # change the element number 5
print(x)

x.append(900)
print(x)
x.extend(range(13))     # Appends with the range(13)
print(x)
x.insert(12,100)                #inserts 100
print(x)
x.remove(x[-1])         # Removes last element
print(x)
x.pop()         # Remove the last element
print(x)
x.pop(0)        # Removes from the beginning
print(x)

