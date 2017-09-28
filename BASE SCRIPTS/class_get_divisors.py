# I made this class to avoid multiple writting the same code.
# Basically the get divisors initial function needed to factorize the number for which the function
# factor_pyprimes which do the job was put inside.
# But I also need to use this faction outside of the function , but can not access it if not outside.
# Therefore, I made a class to be able to access this method and not to make another function with
# same code.


class get_divisors(object):

    '''Made by Bogdan Trif @ 2016-11-15, based on itertools.combinations module
    and with a little help on list(functools.reduce(operator.mul, i) for i in comb)

    :param nr:  int
    :return: a list with the divisors    '''

#     def __init__(self, nr):   # We don't want to initialize the class with a number
#     self.nr = nr


    def factorise(self, nr):
        ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
        from pyprimes import factorise
        return [val for sublist in [[i[0]]*i[1] for i in factorise(nr)] for val in sublist]

    def divisors(self, nr):
        from itertools import combinations
        import functools, operator, gmpy2
        if gmpy2.is_prime(nr) == True or nr == 1 :
            return [1]    # Must be adjusted to [1] if you change on list
        else :
            all_factors =  self.factorise(nr)
            # set_factors=list(set(all_factors))
            comb= set()
            # print(all_factors)
            for i in range(1, len(all_factors)):
                c = set(combinations(all_factors, i) )
                comb.update(c)
                comb_prod = list(functools.reduce(operator.mul, i) for i in comb)
                comb_prod.sort()
        return  comb_prod[::-1]   # sum([1]+ comb_prod)   !!!!!!!! Remember to change on  return [1]  for isprime case


print('\nUsing the method get_divisors from within the class : ', get_divisors().divisors(90) )
print('Using the method factorise from within the class : ', get_divisors().factorise(90)  )