def some_recursion(n):
    if  n < 1e-8 :
        return n
    elif n > 1e8 :
        return n


    print(n)
    return some_recursion(n//2)
    print(n)
    return some_recursion(n*2)


some_recursion(1e3)
