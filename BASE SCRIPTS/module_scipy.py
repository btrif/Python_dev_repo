import scipy

print(help(scipy))
print('-----------------------------------')

print(dir(scipy))

print('\n=====================================\n')
from scipy.integrate import dblquad

area = dblquad(lambda x,y : x*y, 0, 0.5, lambda x: 0, lambda x: 1-2*x)
print(area)

######### Bounded region by y = x, circle : (x-1/2)**2+(y-1/2)**2 = 1/4, x=0

area2 = dblquad(lambda x,y : 1, 0, 0.146, lambda x: x, lambda x: (1/2)-(x-x*x)**(1/2))
print('\n',area2)