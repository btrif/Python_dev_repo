import re
import sys
#from xml.etree import ElementTree as ET


infile = open('pricefx-config.xml.template', 'r')
outfile = open('result_template.txt', 'w')

def main():
    pattern = re.compile('%%.*%%') 
    for line in infile:
        if re.search(pattern, line):
    #           print(line.split("%%", 0), end='')
                print(line, end='')

if __name__ == "__main__": main()            
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
