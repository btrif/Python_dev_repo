import re
import sys



def main():
    
    infile2 = open('pricefx-config.xml', 'r')
    outfile2 = open('result_xml_temp.txt', 'w')    
    
    start_pattern = re.compile('<!--')
    end_pattern = re.compile('-->')
    end_line_pattern = re.compile('\n|[a-z]')
    letter_pattern = re.compile('^\s+([a-z]|[A-Z]|-)')
    
  #setting here the boolean to False will use in the for loop for testing   
    isComment = False
     
    for line in infile2:
        if re.search(start_pattern, line):
            isComment = True
            
        if isComment:
            pass
#            print('comment => ' , line, end='')
        else:
            print(line, end='')
            print(line, file = outfile2, end = '')
                     
        if re.search(end_pattern, line):
            isComment = False
    
    outfile2.close()
    infile2.close()        
    print('Done')
'''    
    infile3 = open(result_xml_temp.txt, 'r')
    outfile3 = open('result_xml.txt', 'w')
                    
    for line in infile3:
            pattern2 = re.compile(r'>.+<')
            match2 = re.search(pattern2, line)
            if match2:
                print(match2.group())
                print(match2.group(), file = outfile3)
'''    
        
'''        
        if re.search(start_pattern, line) and re.search(end_pattern, line):
            var1 = True
            print(line, end='')
#            while var1  == True:
              
        elif re.search(start_pattern, line) and re.search(end_line_pattern, line):
            print(line, end='')
        elif re.search(letter_pattern, line):
            print(line, end='')
        elif re.search(end_pattern, line):
            print(line, end='')                
        else:
            var2 = False
#            print(line, end='')
'''
#    print('============='*10,'\nDone.')   


if __name__ == "__main__": main()            


