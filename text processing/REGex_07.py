import re
import sys
#from xml.etree import ElementTree as ET


infile = open('pricefx-config.xml.template', 'r')
outfile = open('result_template.txt', 'w')

def main():
    pattern = re.compile('%%.+%%') 
    for line in infile:
        match = re.search(pattern, line)
        if match:
            print(match.group(), file = outfile)
    print('Done')

if __name__ == "__main__": main()            


