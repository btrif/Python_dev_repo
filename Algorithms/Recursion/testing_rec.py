#  Created by Bogdan Trif on 24-05-2018 , 11:34 PM.
def test_rec(n):
    if n > 5 :
        print(n)
        test_rec(n-1)
        print(2*n)

test_rec(10)