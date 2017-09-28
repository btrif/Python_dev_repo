import timeit

cy = timeit.timeit('example_cython.test_function(10**7)', setup = 'example_cython.pyx', number =100)

print(cy)
print('Cython is {}x faster '.format(cy))