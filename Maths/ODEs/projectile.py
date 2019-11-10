# All lines like this one that begin with "#" are comments.
# All other lines are program statements.

# Original Author: Jason Harlow
# Date: Feb. 23, 2010

# This program will display the trajectory of a green ball and a yellow ball.
# The yellow ball just uses the equations of motion, which neglect air
# resistance. The green ball is a numerical integration, which computes
# the net force on the ball, finds the acceleration, updates the velocity
# using dv = a*dt, and updates the position using dx = v*dt.

# Press the "F5" key to run the code.  Press the "Esc" key to stop it.
# The program will automatically stop when the green ball hits the floor again.

# Import the visual library (vpython).
from visual import *

##########################################################
###       Variables you might want to change          ####
##########################################################
# The initial speed of the balls: [m/s]
v0 = 30
# The angle above the horizontal at which the balls were launched: [degrees]
theta0 = 45
# The mass of the balls: [kg]
m = 1.0
# The radius of the balls: [m]
r = 0.05
# The "drag coefficient" (see pg.168 of Knight PSE2e): [kg / m^3]
# (Note: Set this equal to zero if you want to see what the animation
# looks like with no air resistance)
d = 0.25
# The time-step of the numerical integration [s]
# (If you set this too large, the numerical approximations of dv=a*dt
# and dx=v*dt will not work well.  If you set this too small, it
# will take the computer a long time to do the computation.)
dt = 0.05

##########################################################
###   Variables you probably DONT want to change      ####
##########################################################
# The acceleration due to gravity [m/s^2]
g = 9.8
# The initial x and y position of the balls [m]
x0 = 0
y0 = 0
# The initial time [s]
t = 0
# Compute the initial x and y components of the velocity
# of the balls: [m/s]
# (Note that in Python, math.sin() and math.cos() are the functions
# for sine and cosine, and they require that the argument be in radians)
vx0 = v0 * math.cos(theta0*3.14159/180)
vy0 = v0 * math.sin(theta0*3.14159/180)
# Compute the cross-section of the spherical green ball: [m^2]
# (Note that in Python, you raise something to the exponent with **,
# not ^)
area = 3.14159 * r**2

##########################################################
###   Making a display on the screen                  ####
##########################################################
# Set up a black window to display on:
scene.autoscale = 0
scene.height = 600
scene.width = 800
scene.range = vector(60, 60, 60)
# Create the green ball:
greenBall = sphere (color = color.green, radius = 2)
# Create the yellow ball:
yellowBall = sphere (color = color.yellow, radius = 2)
# Display the yellow ball on the window. 
# offset the position of the yellow ball by -50 and +10
yellowBall.pos = (x0-50,y0+10, 0)
# draw a yellow line for the floor of the yellow ball.
yellowFloor = curve(pos=[(-60,8),(60,8)], color=color.yellow)
# Display the green ball on the window. 
# offset the position of the green ball by -50 and -20
greenBall.pos = (x0-50,y0-20,0)
# draw a green line for the floor of the green ball.
greenFloor = curve(pos=[(-60,-22),(60,-22)], color=color.green)

##########################################################
###   Now let's do the physics!!                      ####
##########################################################
# Before starting the numerical integration, set the current position
# and velocity of the green ball to be equal to the initial position
# and velocity (the green ball position and velocity have no "green"
# subscript):
x = x0
y = y0
vx = vx0
vy = vy0

# The following indented lines will be executed again and again (in
# a loop) for as long as the position of the green ball is above its
# initial position
while y >= y0:
    
    # First the easy part: compute the position of the yellow ball,
    # using our old equations of kinematics, which neglect air resistance
    xyellow = x0 + (vx0 * t)
    yyellow = y0 + (vy0 * t) - (0.5 * g * t**2)

    # display the position of the yellow ball on the black window:
    yellowBall.pos = (xyellow-50,yyellow+10,0)
    # print the time and position to the screen: 
    print( "t=", t, "s, yellow pos: ", xyellow, yyellow)

    # Find the speed of the green ball right now:
    v = sqrt(vx**2 + vy**2)

    # Find the magnitude of the drag force due to air resistance on the
    # green ball:
    fdrag = d * area * v**2

    # Find the x-component of the net force on the green ball, which will
    # be due to drag force only, in the opposite direction of motion:
    fnetx = fdrag*(-1*vx/v)

    # Find the y-component of net force on the green ball, which will
    # be the sum of the drag force and the downward force of gravity:
    fnety = fdrag*(-1*vy/v) - (m*g)

    # Use Newton's second law to find the acceleration of the green ball:
    ax = fnetx / m
    ay = fnety / m
    
    # Update the velocity of the green ball using the acceleration. Note
    # that we "recycle" the variables vx and vy, replacing the
    # old values with the new ones.
    vx = vx + ax*dt
    vy = vy + ay*dt

    # Update the position of the green ball using the velocity.
    x = x + vx*dt
    y = y + vy*dt

    # display the position of the green ball on the black window:
    greenBall.pos = (x-50, y-20, 0)
    # print the time and position to the screen: 
    print( "t=", t, "s, green pos: ", x, y)
    
    # Update the time, and end the loop!
    t = t + dt

