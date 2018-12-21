#  Created by Bogdan Trif on 16-05-2018 , 10:13 PM.
"""
Solve p = a^2 + b^2 where p is a prime and p = 1 (mod 4)
"""

# https://math.stackexchange.com/questions/5877/efficiently-finding-two-squares-which-sum-to-a-prime

# The web is littered with any number of pages (example) giving an existence and uniqueness proof
# that a pair of squares can be found summing to primes congruent to 1 mod 4
# (and also that there are no such pairs for primes congruent to 3 mod 4).
#
# However, none of the stuff I've read on the topic offers any help with actually efficiently finding ' \
# (ie other than a straight search up to sqrt(p)) the concrete values of such squares.
#
# What's the best way to actually find them ?
#
# number-theory algorithms prime-numbers

class HermiteSerretAlgorithm():
    def get(self, prime):
        if prime % 4 != 1:
            raise ValueError
        x = self.__find_x(prime)
        return self.__apply_brillhart_method(prime, x)

    def __find_x(self, prime):
        half_prime = (prime - 1) // 2
        for a in range(1, half_prime + 1):
            if pow(a, half_prime, prime) == prime - 1:
                return pow(a, (prime - 1) // 4, prime)
        raise ValueError

    def __apply_brillhart_method(self, prime, x):
        if prime % x == 1:
            return (1, x)
        a, b = prime, x
        while b != 0:
            r = a % b
            if r * r < prime:
                return (b % r, r)
            a, b = b, r
        raise ValueError

"""
(a^2 + b^2)(c^2 + d^2) = (ac + bd)^2 + (ad - bc)^2 = (ac - bd)^2 + (ad + bc)^2
"""
class BrahmaguptaFibonacciIdentity():
    def get_one_list_and_another_list(self, one_list, another_list):
        result = set()
        for one in one_list:
            for another in another_list:
                result |= self.get_one_and_another(one, another)
        return result

    def get_one_and_another_list(self, one, another_list):
        result = set()
        for another in another_list:
            result |= self.get_one_and_another(one, another)
        return result

    def get_one_list_and_another(self, one_list, another):
        result = set()
        for one in one_list:
            result |= self.get_one_and_another(one, another)
        return result

    def get_one_and_another(self, one, another):
        result = set()
        a, b = one
        c, d = another
        x, y = abs(a * c - b * d), a * d + b * c
        if x > y:
            result.add((y, x))
        else:
            result.add((x, y))
        x, y = a * c + b * d, abs(a * d - b * c)
        if x > y:
            result.add((y, x))
        else:
            result.add((x, y))
        return result

class FactorizationAlgorithm():
    def __init__(self, n):
        self.values = self.__get_values(n)

    def __get_values(self, n):
        values = [{} for i in range(n + 1)]
        for i in range(2, n + 1):
            if values[i]:
                continue
            for j in range(i, n + 1, i):
                values[j][i] = 1
            d = i * i
            while d <= n:
                for j in range(d, n + 1, d):
                    values[j][i] += 1
                d *= i
        return values

    """
    Get the factorization of a * b.
    """
    def get(self, a, b):
        result = {}
        for p in self.values[a]:
            result[p] = self.values[a][p]
        for q in self.values[b]:
            if q not in result:
                result[q] = 0
            result[q] += self.values[b][q]
        return result

"""
Solve n = a^2 + b^2.
"""
class SumsOfTwoSquaresAlgorithm():
    def __init__(self):
        self.one_sum_pair = (0, 1)
        self.two_sum_pair = (1, 1)
        self.hermite_serret_algorithm = HermiteSerretAlgorithm()
        self.brahmagupta_fibonacci_identity = BrahmaguptaFibonacciIdentity()
        self.solution_cache = {}

    def get(self, factorization):
        result = set()
        if not self.__has_solution(factorization):
            return result

        result.add(self.one_sum_pair)
        scalar = 1
        for p in factorization:
            e = factorization[p]
            if p == 2:
                if e % 2 == 1:
                    result = self.brahmagupta_fibonacci_identity.get_one_list_and_another(result, self.two_sum_pair)
                scalar *= p**(e // 2)
            elif p % 4 == 3:
                scalar *= p**(e // 2)
            else:
                prime_factor_solution = self.__get_prime_factor_solution(p, e)
                result = self.brahmagupta_fibonacci_identity.get_one_list_and_another_list(result, prime_factor_solution)
        return self.__multiply_scalar(result, scalar)

    def __has_solution(self, factorization):
        for p in factorization:
            e = factorization[p]
            if p % 4 == 3 and e % 2 == 1:
                return False
        return True

    def __get_prime_factor_solution(self, p, e):
        n = pow(p, e)
        if n not in self.solution_cache:
            result = set()
            primitive_pair = self.hermite_serret_algorithm.get(p)
            result.add(primitive_pair)
            for i in range(2, e + 1):
                result = self.brahmagupta_fibonacci_identity.get_one_list_and_another(result, primitive_pair)
            self.solution_cache[n] = result
        return self.solution_cache[n]

    def __multiply_scalar(self, solution, scalar):
        result = set()
        for x, y in solution:
            result.add((x * scalar, y * scalar))
        return result


FA = FactorizationAlgorithm(100)
FA.get(4, 25)