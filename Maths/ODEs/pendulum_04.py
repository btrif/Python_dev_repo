# Implementing the Euler-Cromer Method for a set number of data points
from __future__ import division
from math import *
from scipy import *
import matplotlib.pyplot as plt
# Initial theta values
theta0 = (10*2*pi)/360
omega0 = 5*2*pi/360
# Constants
length_of_string = 9.8
gravity = 9.8
drive_frequency = 1/3
damping_force = 0.05
# Defining the driving force - controls the chaos
FD = 0.01
# Assigning the number of data points to be considered
data_points = 3700
# Preallocating space for time, theta and omega
time = zeros(data_points)
theta = zeros(data_points)
omega = zeros(data_points)
# Initializing theta and omega
theta[0] = theta0
omega[0] = omega0
# Defining time step size
dt = 0.05
for i in range(0, data_points-1):
 time[i+1] = time[i] + dt
 # Calculating for FD = 0, 0.1... in omegas

 omega[i+1] = omega[i] - (gravity/length_of_string)*sin(theta[i])*dt - (
 damping_force*omega[i]*dt + FD*sin(drive_frequency*time[i])*dt)
 theta[i+1] = theta[i] + omega[i+1]*dt
plt.plot(time, theta)
plt.ylabel("theta")
plt.xlabel("time")
plt.show()
