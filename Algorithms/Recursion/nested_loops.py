#  Created by Bogdan Trif on 21-11-2017 , 10:30 PM.
# While itertools is the way to go, this question is an excellent exercise for practicing generator functions:      !!!!!!!!!!

print('\n ####### METHOD 3 - RECURSION - ELEGANT, BEAUTIFUL, Must learn it ############  ')

def multirange_rec(d):
    if len(d) == 1:
        for i in range(d[0]):
            yield [i]
    elif len(d) > 1:
        for i in range(d[-1]):
            for a in multirange_rec(d[:-1]):
                yield a + [i]

def multirange_iter(d):
    l = len(d)
    products = [1]
    for k in d:
        products.append(products[-1]*k)
    n = products[-1]
    for i in range(n):
        yield [(i%products[j+1])//products[j] for j in range(l)]

for l in multirange_rec([4,3,2]):
    print(l , end='  ')

print()
for l in multirange_iter([4,3,2]):
    print(l, end = '  ')
