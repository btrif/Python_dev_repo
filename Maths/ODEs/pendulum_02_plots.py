from scipy import *
from matplotlib.pyplot import *
##A pendulum simulation using fourth order 
##Runge-Kutta differentiation

ts=.05 #time step size
td=20 #trial duration
te=int(td/ts) #no of timesteps

mu=0.1 #friction factor
m=1 #mass
g=9.81 #grav. acceleration
l=1 #length

th=[((rand()*2)-1)*pi] #initial angle
om=[0] #initial angular velocity
u=0 #torque

for j in range(te):
    #Euler approximation
    th.append(th[j] + ts*om[j])
    f1 = (-mu*om[j] + m*g*l*sin(th[j]) + u)/(m*(l**2))
    om.append(om[j] + ts*f1)

    #approximation 1 at mid-interval
    th2 = th[j+1] + (ts/2)*om[j+1]
    f2 = (-mu*om[j+1] + m*g*l*sin(th[j+1]) + u)/(m*(l**2))
    om2 = om[j+1] + (ts/2)*f2

    #approximation 2 at mid-interval
    th3 = th2 + (ts/2)*om2
    f3 = (-mu*om2 + m*g*l*sin(th2) + u)/( m*(l**2))
    om3 = om2 + (ts/2)*f3

    #approximation at next time step
    th4 = th3 + (ts)*om3
    f4 = (-mu*om3 + m*g*l*sin(th3) + u)/( m*(l**2))
    om4 = om3 + (ts)*f4

    dth=(om[j] + 2*om[j+1] + 2*om2 + om3)/6
    dom=(f1 + 2*f2 + 2*f3 + f4)/6
    th[j+1] = th[j] + ts*dth
    om[j+1] = om[j] + ts*dom

subplot(211),plot(th),xlabel('Angle'),ylabel('')
subplot(212),plot(om,'r'),xlabel('Angular velocity'),ylabel('')
show()