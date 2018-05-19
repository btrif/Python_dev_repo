#!/usr/bin/python3
# Bogdan Trif @ 2014 OCT 30, 16:10

def main():
    s = 'this is very nice string, boy'
    for i, c in enumerate(s):
        if c =='s': print('index {} is an s'.format(i))
        

if __name__ == "__main__": main()
