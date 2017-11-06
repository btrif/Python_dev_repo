import time

t1  = time.time()

def palin_generator(up_range):
    palindromes = [1,2,3,4,5,6,7,8,9]
    """Generates palindromic numbers."""
    if len(str(up_range)) % 2 == 1 :
        l = int(len(str(up_range))/2)
    elif len(str(up_range)) % 2 == 0 :
        l = int(len(str(up_range))/2)
    print('for orientation: ', len(str(up_range)) , l   )


    for i in range(1, 10) :
        # palindromes.append( int( str(i)+str(i)[:-1][::-1]) )
        palindromes.append( int(str(i)+str(i)[::-1 ] )   )

    for i in range(10, 10**(l) ):
        s1 = int( str(i)+str(i)[:-1][::-1])
        s2 =  int(str(i)+str(i)[::-1 ] )
        if s1 < up_range : palindromes.append( s1   )
        if s2 < up_range : palindromes.append( s2   )
        # if l% 2 == 1 :      # is Odd, like 123 , We want to add only the numbers 12321 because of the range
        #     palindromes.append( int( str(i)+str(i)[:-1][::-1]) )
        # if l% 2 == 1 :      # is Even, like 1234, We want to add both 1234321 and 12344321
        #     palindromes.append( int( str(i)+str(i)[:-1][::-1]) )
        #     palindromes.append( int(str(i)+str(i)[::-1 ] )   )

    return palindromes

Pal = palin_generator(10**4)
print( len(Pal),'\n' , sorted(Pal) )


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



def makePalindrome_mhb038(n,base,oddlength):
    res = n
    if oddlength:
        n = n // base
    while n > 0:
         res = base*res + n % base
         n = n // base
    return res





# Algorithm: If replacing the right half of the original number with the
# mirror of the left half results in a bigger number, return that.
# Otherwise, increment the left half of the number, then replace the
# right half of the original number with the mirror of the new left half
# and return.

def next_palindrome(n):
    X = len(n)>>1
    Y = X+(len(n)&1)
    first = n[X-1::-1]
    second = n[Y:]
    Z = n[:Y]
    assert Y >= X        #, "by construction"
    assert len(second) >= len(first)        #, "by construction"
    if len(first) == len(second) and first > second:
        assert int(first) > int(second)         #, "because ASCII"
        return Z+first
    # if int(first) > int(second):
    #     return Z+first
    else:
        bar = str(int(Z)+1)
        return bar+bar[:X][::-1]







print('next_palindrome : \t', next_palindrome('11'))
print('next_palindrome : \t', next_palindrome('111'))
print('next_palindrome : \t', next_palindrome('835'))
print('next_palindrome : \t', next_palindrome('5384'))


print('\n--------------- Palindrome Generator -------------------')

def next_palindrome_gen(n):
    X = len(n)>>1
    Y = X+(len(n)&1)
    first = n[X-1::-1]
    second = n[Y:]
    Z = n[:Y]
    assert Y >= X        #, "by construction"
    assert len(second) >= len(first)        #, "by construction"
    if len(first) == len(second) and first > second:
        assert int(first) > int(second)         #, "because ASCII"
        yield Z+first
    # if int(first) > int(second):
    #     return Z+first
    else:
        bar = str(int(Z)+1)
        yield bar+bar[:X][::-1]

G = next_palindrome_gen('10000000')
for i in range(10):
    p = next(G)
    print(str(i+1)+'.  ', p, end='      ')
    G = next_palindrome_gen(str(p))


####################

def palindrome_gen():
    """
    Generates palindromicall numbers from the
    smallest by value.

    >>> take(12, palindrome_gen())
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22]

    >>> nth(palindrome_gen(), 19)
    101

    >>> nth(palindrome_gen(), 20)
    111

    >>> it = palindrome_gen()
    >>> consume(it, 19)
    >>> take(11, it)
    [101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202]

    >>> it = palindrome_gen()
    >>> consume(it, 10 + 9 + 10 * 9)
    >>> take(14, it)
    [1001, 1111, 1221, 1331, 1441, 1551, 1661, 1771, 1881, 1991, 2002, \
2112, 2222, 2332]

    """
    odd_half = 0
    odd_val = int(str(odd_half) + str(odd_half)[::-1][1:])
    even_half = 1
    even_val = int(str(even_half) + str(even_half)[::-1])
    while True:
        if odd_val < even_val:
            odd_half += 1
            yield odd_val
            odd_val = int(str(odd_half) + str(odd_half)[::-1][1:])
        else:
            even_half += 1
            yield even_val
            even_val = int(str(even_half) + str(even_half)[::-1])
