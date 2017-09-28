import re
import sys
#from xml.etree import ElementTree as ET

# Define the search term:
pattern = '%%'

# Create an empty list:

fh = open('pricefx-config.xml.template', 'r')

# def main():
    
for line in fh:
    if re.search(pattern, line):
#           print(line.split("%%", 0), end='')
            print(line, end='')
            
#fh.write()

# if __name__ == "__main__": main()

# Read the entire XML file
'''
def main():
    fh = open('pricefx-config.xml.template', 'r')
    for line in fh.readlines():
        print(line)

if __name__ == "__main__": main()
'''
