
def is_prime(n):
    i = n
    while(i <= n):
        j = 2
        while(j <= (i/j)):
            if not(i%j):
                print(i, ' is NOT prime')
                break
            j = j + 1
        if (j > i/j) : print( i, " is prime")
        i = i + 1


def detect_prime(n):
    i = n
    while(i <= n):
        j = 2
        while(j <= (i/j)):
            if not(i%j):
                return False
                break
            j = j + 1
        if (j > i/j) : return True
        i = i + 1

#is_prime(999999999269)
#print(detect_prime(95) == detect_prime(98))



