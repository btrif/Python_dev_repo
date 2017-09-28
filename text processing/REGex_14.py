import re
import sys

infile2 = open('pricefx-config.xml', 'r')
#infile2 = open('html.html', 'r')
outfile2 = open('result_xml.txt', 'w')

def main():
    
    start_pattern = re.compile('<!--')
    end_pattern = re.compile('-->')
    end_line_pattern = re.compile('\n|[a-z]|[0-9]|\.')
    letter_pattern = re.compile('^\s+([a-z]|[A-Z]|-)') 
     
    for line in infile2:
        if re.search(start_pattern, line) and re.search(end_pattern, line): continue
#            var1 = True
#            print(line, end='')
#            while var1  == True:
        elif re.search('^\s+$', line) : continue
        elif re.search('^\s+</|^</|^\s+<.+', line) : continue      
        elif re.search(start_pattern, line) and re.search(end_line_pattern, line): continue
#            print(line, end='')
        elif re.search(letter_pattern, line): continue
#            print(line, end='')
        elif re.search(end_pattern, line): continue
#            print(line, end='')                
        else:
            var2 = False
            print(line, end='')

    print('============='*10,'\nDone.')   


if __name__ == "__main__": main()            


