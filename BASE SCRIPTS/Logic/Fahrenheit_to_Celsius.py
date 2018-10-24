#!/usr/bin/python3
# -*- coding: iso-8859-15 -*-
import sys

try:
	C = float(sys.argv[1])
except:
	print ("You failed to provide Celsius degrees as input on the command line!")
    
	sys.exit(1)  # abort

F = 9.0 * C / 5 + 32

print(C, 'C =', F, ' F')
