from numpy import *#Imports Python mathematical functions library
import matplotlib.pyplot as plt #Imports plot library
from pylab import *

a = 5
e = 0.3
theta = 0

points = []
while theta <= 2*pi:
    r = (a*(1-e**2))/(1+e*cos(theta))
    print("r = ",r,"theta = ",theta)
    points.append((theta, r))
    theta += pi/180

#plt.polar(points) #this is cool but probably not what you want
plt.polar(*zip(*points))
plt.show()