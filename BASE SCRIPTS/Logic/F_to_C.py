'''
Python Program to convert temperature in  Celsius to Fahrenheit where, input is
 provided by the user in  degree celsius
'''
# -*- coding:latin-1 -*-
# input=raw_input
# take input from the user

celsius = input('Enter degree Celsius: ')

try:
    celsius = float(celsius)
    fahrenheit = (celsius * 1.8) + 32
    print(celsius, ' degrees C = ', fahrenheit, ' degrees F')
except ValueError:
   print("That's not an int or float!")
