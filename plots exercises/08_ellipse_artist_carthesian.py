import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

# initializing the figure:
fig = plt.figure()

# the (carthesian) axis:
ax = fig.add_subplot(111,aspect='equal')
ax.grid(True)

# parameters of the ellipse:
a = 5.0
e = 4.0
b = np.sqrt(a**2.0 - e**2.0)

# the center of the ellipse:
x = 6.0
y = 6.0

# the angle by which the ellipse is rotated:
angle = -45.0
#angle = 0.0

# plotting the ellipse, using an artist:
ax.add_artist(Ellipse(xy=[x,y], width=2.0*a, height=2.0*b, \
                                angle=angle, facecolor='none'))
ax.set_xlim(0,2.0*x)
ax.set_ylim(0,2.0*y)

# marking the focus (actually, both)
# and accounting for the rotation of the ellipse by angle
xf = [x - e*np.cos(angle * np.pi/180.0),
      x + e*np.cos(angle * np.pi/180.0)]

yf = [y - e*np.sin(angle * np.pi/180.0),
      y + e*np.sin(angle * np.pi/180.0)]

ax.plot(xf,yf,'xr')

# plotting lines from the focus to the ellipse:
# these should be your "rays"
t = np.arange(np.pi,3.0*np.pi,np.pi/5.0)
p = b**2.0 / a
E = e / a
r = [p/(1-E*np.cos(ti)) for ti in t]

# converting the radius based on the focus 
# into x,y coordinates on the ellipse:
xr = [ri*np.cos(ti) for ri,ti in zip(r,t)]
yr = [ri*np.sin(ti) for ri,ti in zip(r,t)]

# accounting for the rotation by anlge:
xrp = [xi*np.cos(angle * np.pi/180.0) - \
       yi*np.sin(angle * np.pi/180.0) for xi,yi in zip(xr,yr)]
yrp = [xi*np.sin(angle * np.pi/180.0) + \
       yi*np.cos(angle * np.pi/180.0) for xi,yi in zip(xr,yr)]

for q in range(0,len(t)):
    ax.plot([xf[0], xf[0]+xrp[q]],[yf[0], yf[0]+yrp[q]],'--b')

# put labels outside the "rays"
offset = 0.75
rLabel = [ri+offset for ri in r]
xrl = [ri*np.cos(ti) for ri,ti in zip(rLabel,t)]
yrl = [ri*np.sin(ti) for ri,ti in zip(rLabel,t)]

xrpl = [xi*np.cos(angle * np.pi/180.0) - \
        yi*np.sin(angle * np.pi/180.0) for xi,yi in zip(xrl,yrl)]
yrpl = [xi*np.sin(angle * np.pi/180.0) + \
        yi*np.cos(angle * np.pi/180.0) for xi,yi in zip(xrl,yrl)]

# for fancy label rotation reduce the range of the angle t:
tlabel = [(ti -np.pi)*180.0/np.pi for ti in t]
for q in range(0,len(tlabel)):
    if tlabel[q] >= 180.0:
        tlabel[q] -= 180.0

# convert the angle t from radians into degrees:
tl = [(ti-np.pi)*180.0/np.pi for ti in t]

for q in range(0,len(t)):
    rotate_label = angle + tlabel[q]
    label_text = '%.1f' % tl[q]
    ax.text(xf[0]+xrpl[q],yf[0]+yrpl[q],label_text,\
            va='center', ha='center',rotation=rotate_label)

plt.show()