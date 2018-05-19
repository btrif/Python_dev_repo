primes = [2, 3, 5, 7, 11]

x = int(input("Please enter an integer between 2 and 168: \n"))

# Make a guess
isPrime = True

# go through a list to determine if our guess was wrong

for p in primes:
    
    if x % p == 0 and not x in primes:
        isPrime = False
        
if isPrime:
    print(x, "is Prime.")
else:
    print(x, "is not prime.")
