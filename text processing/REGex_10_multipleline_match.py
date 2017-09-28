import re
import sys


#infile1 = open('pricefx-config.xml.template', 'r')
#outfile1 = open('result_template.txt', 'w')
#infile2 = open('pricefx-config.xml', 'r')
infile2 = open('html.html', 'r')
outfile2 = open('result_xml.txt', 'w')

def main():
    buffersize = 50000
    buffer = infile2.read(buffersize)
#    pattern2 = re.compile('<!--((.+|.+\n.|\r)*)-->')
#    pattern2 = re.compile(r'<!--((.+|.+\n|.\n|.+\n.+).+)-->')  
#    pattern2 = re.compile(r'<!--.*-->', re.DOTALL)  
#    while len(buffer):
#        print(buffer)
#        print('.', end = '')
 #       buffer = infile2.read(buffersize)
#    print(buffer)

    while len(buffer) :
#    match2 = re.search('<p>.*</p>', buffer, re.DOTALL)
        match2 = re.search(r'<!--.*-->', buffer, re.DOTALL)
        outfile2.write(buffer)
        buffer = infile2.read(buffersize)    
        print(match2.group(), end='')
#    print(match2)

#print('Done')

if __name__ == "__main__": main()            


