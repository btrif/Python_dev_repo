from numpy import linspace
from scipy import pi, sin, cos


def ellipse(ra , rb , ang , x0 , y0 , Nb=500):
	'''ra - major axis length
	  rb - minor axis length
	  ang - angle
	  x0, y0 - position of centre of ellipse
	  Nb - No. of points that make an ellipse
	  
	  based on matlab code ellipse.m  written by D.G. Long, 
	  Brigham Young University, based on the
	  CIRCLES.m original 
	  written by Peter Blattner, Institute of Microtechnology, 
	  University of  Neuchatel, Switzerland, blattner@imt.unine.ch
	'''
#	xpos , ypos = x0 , y0
	#radm , radn = ra , rb
#	an = ang
#	co , si = cos(ang), sin(ang)
	the = linspace(0 , 2*pi , Nb)

	X = ra * cos(the) * cos(ang) - sin(ang) * rb * sin(the) + x0
	Y = ra * cos(the) * sin(ang) + cos(ang) * rb * sin(the) + y0

	return X,Y

def test():
	import pylab as p
	
	fig = p.figure(figsize=(12 , 12))
	p.axis([-3 , 3 , -3,3])

	#eg 1
	X,Y=ellipse(2 , 1 , pi * 2.0/3.0 , 0 ,1, Nb = 20)
	p.plot(X, Y, "b.-", ms=1) # blue ellipse
	
	#eg 2
	X,Y=ellipse(2 , 0.5 , pi/3.0 , 1 , 1)
	p.plot(X , Y ,"r.-" , ms=1) # red ellipse

	#eg 3
	X,Y=ellipse(1 , 1.2 , pi/3.0 , 0 , 0 , Nb=16)
	p.plot(X, Y , "g.-" , ms=1) # green ellipse
	
	p.grid(True)
	p.show()

	
if __name__ == '__main__': 
	test()