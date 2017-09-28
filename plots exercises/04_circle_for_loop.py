# I wish I had payed more attention in my calculus class
# when I was at school. Could have saved me ages.
 
from math import sin,cos,pi
import matplotlib.pyplot as plt
 
# use radians instead of degrees - OBVIOUSLY!! 
list_radians = [0]
 
# from degrees to radians, the 0 is already included so
# we don't make the universe collapse by dividing by zero.
for i in range(0,360):
    float_div = 180.0/(i+1)
    list_radians.append(pi/float_div)
     
# list of coordinates for each point
list_x2_axis = []
list_y2_axis = []
 
# calculate coordinates 
# and append to above list
for a in list_radians:
    list_x2_axis.append(cos(a))
    list_y2_axis.append(sin(a))
    
#fig = plt.figure()
plt.figure().add_subplot(111,aspect='equal')  

     
# set axis limits
plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)
 
# plot the coordinates        ,aspect='equal'
plt.plot(list_x2_axis,list_y2_axis,c='r')
 
# show the plot
plt.grid(b=True, which='both', color='0.65',linestyle='--')
plt.show()