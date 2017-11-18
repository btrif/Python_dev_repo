import random, time



def Miller_Rabin(p, k = 50):  # Miller-Rabin primality test
    if p == 2: return True
    if p < 2 or p & 1 == 0: return False

    d = (p - 1) >> 1
    while d & 1 == 0:
        d >>= 1

    for i in range(k):
        a = random.randint(1, p - 1)
        t = d
        y = pow(a, t, p)
        while t != p - 1 and y != 1 and y != p - 1:
            y = pow(y, 2, p)
            t <<= 1
        if y != p - 1 and t & 1 == 0:
            return False
    return True

t1  = time.time()


print( Miller_Rabin(151681868531) )
print( Miller_Rabin(931609520341274652367578460852510282407178386733656844055367044369114498629648976054002050099910463009) )


t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')