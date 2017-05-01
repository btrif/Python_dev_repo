title = " bogdan, please don't die with the music still in you"
# A first Python script
import sys  # Load a library module
print("vesiunea platformei:" + sys.platform + "\nVersiunea de Python:" + sys.version)
# print(sys.*)
s = 2 ** 100
print ("2 la puterea 100 este =", s, "\n Nu-i asa ?")  # Raise 2 to a power
x = 'Spam!'
print(x * 18)  # String repetition

a = 'Love'
b = ' Comes'
c = 'Again'
d = ', by DJ Tiesto'
print(a, b, c, d)

#input()     # this stops the script and wait input from user, with simple parantheses it just waits and never stops

import subprocess
# This call the Windows executable cmd and outputs the content of the current directory
subprocess.call(['C:\\windows\\system32\\cmd.exe', '/C', 'dir'])