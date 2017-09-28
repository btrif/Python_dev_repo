# Euler Pb 091
from itertools import *
# print(sum((a[0]+a[1]==a[2] for a in (sorted((p[0]**2+p[1]**2, q[0]**2+q[1]**2, (p[0]-q[0])**2+(p[1]-q[1])**2)) for (p,q) in combinations(product(range(51),range(51)),2)) if a[0]>0)))


tags = [u'man', u'you', u'are', u'awesome']
entries = [[u'man', u'thats'],[ u'right',u'awesome']]
# [entry for tag in tags for entry in entries if tag in entry]


lst1=['1035', '1000', '3000', '7600', '1225', '1275', '1326']
lst2=['3510', '1081', '3528', '1176', '2512', '1275', '1300']
print([x for x in lst1 if  x in lst2])

lst = ['abc-123', 'def-456', 'ghi-789', 'abc-456']
print (filter(lambda x: 'abc' in x, lst))
print([x for x in lst if '456' in x])

lizt = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print([x for y in lizt if sum(y)>10 for x in y if x < 10])

matchers = ['abc','def']
print([s for s in lst if any(xs in s for xs in matchers)])

#############################
print('\n-----------------Intersection of two lists, but only the last digits from lst1 with first two digits of lst2-----------')
lst1=['1035', '1046', '3000', '7639', '1225', '1275', '1326']
lst2=['3510', '1081', '3528', '1176', '2512', '1275', '1376']
matchers = [i[2:] for i in lst1]
print(matchers)
print([s for s in lst2 if any(y in s[:2] for y in matchers)])
print('---------------------------------------')