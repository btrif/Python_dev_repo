# import time

def test_function(x):
    y = 0
    for i in range(x):
        y += i
    return y


# t1  = time.time()
#
#
# print('test function:    ' , test_function(10**7) )
#
#
# t2  = time.time()
# print('Completed in :', round((t2-t1)*1000,6), 'ms\n\n')

