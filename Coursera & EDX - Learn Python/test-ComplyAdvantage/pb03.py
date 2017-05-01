
def memoize(f):
    """ Memoization decorator for functions taking one or more arguments. """
    class memodict(dict):
        def __init__(self, f):
            self.f = f
        def __call__(self, *args):
            return self[args]
        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret
    return memodict(f)

class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]


def solution(A, B):
    # vmax = 0
    @Memoize
    def P(n) :
        if n ==0 :  return 1
        return ( A * P(n-1) ) % B

    N = set()
    for n in range( B+1) :
        # if P(n) > vmax :
        #     vmax = P(n)
        if P(n) == B-1 : return B-1
        if  P(n) in N :
            return max(N)
        N.add(P(n) )
        # print( str(n)+'.     ' ,P(n)  )

print('\n' ,solution( 2046, 1481) )

print('\n --------------------------- TEST CASES ---------------------------- ')


def automatic_tests() :
    import random

    for i in range(1,100) :
        a, b = random.randint( 11, 3000 ) , random.randint( 11, 3000 )
        print(str(i)+'.         a,b=',a,b ,'             solution=' ,solution(a,b)  )

automatic_tests()
