
# Multiplication Table

print("    ", end="")
for i in range(16):
    print("%4d|" % i, end="")
    
print()
print('------' * 14)

for i in range(16):
    print ("%4d|" % i, end="")
    
    for j in range(16):
        print("%4d|" % (i * j), end="")
        
    print()
