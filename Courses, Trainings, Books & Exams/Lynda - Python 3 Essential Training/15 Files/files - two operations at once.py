# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

# FIRST METHOD
for line in fh:
        upper=line.upper()
        print(upper.rstrip())
print('-----'*10)
# SECOND METHOD   -  BETTER !
for xx in fh:
        xx = xx.rstrip().upper()        # that's how you do more operations on a string  !
        print(xx)

