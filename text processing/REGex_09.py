import re
import sys
#from xml.etree import ElementTree as ET


#infile1 = open('pricefx-config.xml.template', 'r')
#outfile1 = open('result_template.txt', 'w')
infile2 = open('result_xml_temp.txt', 'r')
outfile2 = open('result_xml.txt', 'w')

def main():
    
    pattern2 = re.compile('>.+<')  
    for line2 in infile2:
        match2 = re.search(pattern2, line2)
        if match2:
            print(match2.group())
            print(match2.group(), file = outfile2)

    print('Done')

if __name__ == "__main__": main()            


