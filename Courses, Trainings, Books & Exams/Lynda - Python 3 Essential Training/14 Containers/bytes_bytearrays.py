from idlelib.IOBinding import encoding

def main():
    fin = open('utf8.txt', 'r', encoding='utf_8')
    fout = open('utf8.html', 'w')
    
    # Innitialize a byte  array: ( a MUTABLE list of bytes )
    outbytes = bytearray()      # Innitialize a byte array of bytes: ( a mutuable list of bytes )
    for line in fin:
        for c in line:          #loop through the line (iterate through the line)
            if ord(c) > 127:    # bytes are IMMUTABLE ARRAYS OF BYTES
                outbytes += bytes('&#{:04d};'.format(ord(c)), encoding = 'utf_8')
            else: outbytes.append(ord(c))
    outstr = str(outbytes, encoding = 'utf_8')
    print(outstr, file = fout)
    print(outstr)
    print('Done.')

if __name__ == "__main__": main()
