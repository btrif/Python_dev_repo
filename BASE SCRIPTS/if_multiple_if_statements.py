import random

n_trials = 550
n_hits = 0

for iter in range(n_trials):
    x, y = random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)
    if (abs(x) < 0.1 and abs(y) > 0.9 ):        # Multiple if statements
        print(x , y)


print('\n------------- Variable Assignment--------------')
a = 0
b = 2
print(' a, b =   ',a,b)
m = a if a else 9
n = b if b else 9
print(' m, n =  ',m, n)
