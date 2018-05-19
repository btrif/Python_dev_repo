#!/usr/bin/python3

def main():
    a, b = 10 , 1
    if a < b:
        print('This is TRUE')
        
    else:
        print('This is FALSE')


           
    c, d = 4 , 9
    if True:               # I can (replace) put any expression which evaluates to TRUE of FALSE
        print('This is TRUE')
        
    else:
        print('This is FALSE')
 
 
        
    g, h = 4 , 9
    if False:               # I can (replace) put any expression which evaluates to TRUE of FALSE
        print('This is TRUE')
        
    else:
        print('This is FALSE')

if __name__ == "__main__": main()
