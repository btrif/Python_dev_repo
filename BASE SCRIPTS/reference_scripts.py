import re

def main():
    fh = open('raven.txt')
    pattern = re.compile('(Len|Neverm)ore', re.IGNORECASE)
    for line in fh:
        if re.search(pattern, line):
            print(line, end='')

print('-----'*10)

print('-----'*10)


def main():
    fh = open('raven.txt')
    for line in fh:
        match = re.search('(Len|Neverm)ore', line)
        if match:
            print(match.group())

if __name__ == "__main__": main()

print('-----'*10)

def main():
    infile = open('lines.txt','r')
    outfile = open('new.txt', 'w')
    
    for line in infile:
        print(line, file = outfile, end='')
    print('Done.')

print('-----'*10)

def main():
    testfunc()

def testfunc():
    print('This is a test function')

if __name__ == "__main__": main()

print('-----'*10)

def main():
    buffersize = 50000
    infile = open('bigfile.txt','r')
    outfile = open('new_big.txt', 'w')
    buffer = infile.read(buffersize)
    while len(buffer):
        outfile.write(buffer)
        print('.', end = '')
        buffer = infile.read(buffersize)
    print()

print('-----'*10)

def main():
    s = 'this is a string'
    for c in s:
        if c == 's': break   #break = jumps the loop entirely
        print(c, end='')

if __name__ == "__main__": main()

print('-----'*10)
	
def main():
    s = 'this is a string'
    for c in s:
        if c == 's': continue   #continue shortcuts the loop
        print(c, end='')

if __name__ == "__main__": main()


print('-----'*10)


for n in range(2, 16):
     for x in range(2, n):
         if n % x == 0:
             print(n, 'equals', x, '*', n // x)
             break
     else:
         # loop fell through without finding a factor
        print(n, 'is a prime number')

print('-----'*10)