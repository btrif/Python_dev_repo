#!/usr/bin/python

def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action,)
    print("if you put", voltage, "volts through it.",)
    print("E's", state, "!")

# Define a dictionary

d = {"voltage": "4.000.000", "state": "bleedin' demised", "action": "VOOM"}

# call the function parrot with the dictionary

parrot(**d)
