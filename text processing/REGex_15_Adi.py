# Oct 2014, by Bogdan Trif with Adi Moldovan contribution
#

import re
import sys


def remove_comments(infile, outfile):
    start_pattern = re.compile('<!--')
    end_pattern = re.compile('-->')
    end_line_pattern = re.compile('\n|[a-z]')
    letter_pattern = re.compile('^\s+([a-z]|[A-Z]|-)') 
    isComment = False
     
    for line in infile:
        if re.search(start_pattern, line):
            isComment = True
            
        if isComment:
            print("comment => " + line)
            # outfile.write(line)
        else:
            print("no comment => "+ line)
            outfile.write(line)
            
        if re.search(end_pattern, line):
            isComment = False

    outfile.close()

if __name__ == "__main__":

    infile = open('pricefx-config.xml', 'r')
    #infile2 = open('html.html', 'r')
    outfile = open('result_xml.txt', 'w')
    remove_comments(infile , outfile )


