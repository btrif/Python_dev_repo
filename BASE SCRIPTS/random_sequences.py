import random

#    Generate a random hex number, appropriate for CODE COLORS
r = lambda: random.randint(0,255)
print('#%02X%02X%02X' % (r(),r(),r()))

# Second approach
print('--------------# Second approach --------------')
color = "#%06x" % random.randint(0,0xFFFFFF)
print(color)

# To generate a random 3 char color:
print('----------------- To generate a random 3 char color:  ---------')

color = "%03x" % random.randint(0,0xFFF)
print(color)

#-------------------------------------------------------
# Another more intricate way
print('-----   Another more intricate way : ---------')
def hex_code_colors():
    a = hex(random.randrange(0,256))
    b = hex(random.randrange(0,256))
    c = hex(random.randrange(0,256))
    a = a[2:]
    b = b[2:]
    c = c[2:]
    if len(a)<2:
        a = "0" + a
    if len(b)<2:
        b = "0" + b
    if len(c)<2:
        c = "0" + c
    z = a + b + c
    return "#" + z.upper()

print(hex_code_colors())


## Function to generate Random hex
print('---------## Function to generate Random hex ----------------')

def gen_hex_colour_code():
   return "#"+''.join([random.choice('0123456789ABCDEF') for x in range(6)])

print (gen_hex_colour_code())

'''
You could then put this in a separate file called for example, myutilities.py

Then in your main python file, you would use it like this:
'''

import myutilities

print (myutilities.gen_hex_colour_code())

'''
The if __name__ == '__main__': part will only get executed if you run the myutilities.py file directly.
It will not execute when you import it from another file. This is generally where testing functions go.
'''
#---------------------------------------------------------
'''One compact way to do this is to use list comprehensions (which are a certain kind of for loop):'''

alpha = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", 
             "A", "B", "C", "D", "E", "F")
''.join([random.choice(alpha) for _ in range(6)])
'''
Or simply just use a string:
'''
alpha = "ABCDEF0123456789"

#--------------------------------------------------------

'''PS. Since colors are hex, why not just generate a random number and turn it to hexadecimal?'''

hex(random.randint(0, 16777215))[2:].upper()


#----------------------------------------------------------
