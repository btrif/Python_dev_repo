import random

n_trials = 5500000
n_hits = 0
for iter in range(n_trials):
    x, y = random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)
#    print('x:',x,'x^2:',x**2, 'y:',y, 'y^2:', y**2,' ', x**2+y**2 )
    if x**2 + y**2 < 1.0:
       
        n_hits += 1
#        print (4.0 * n_hits / float(n_trials))
#    if (abs(x) < 0.1 and abs(y) > 0.9 ):
#        print(x , y)

print (4.0 * n_hits / float(n_trials), n_hits, n_trials, n_hits/n_trials)
print (n_hits / n_trials * 4 )
print ("The actual value of Pi is:"n_hits / n_trials * 4 )

'''

'''
