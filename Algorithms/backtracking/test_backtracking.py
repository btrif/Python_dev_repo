#  Created by Bogdan Trif on 18-05-2018 , 11:46 AM.

P = [ 2, 3, 5, 7 ]

## Generate all combinations by BACKTRACKING  ( only once , not reapeated ) :

def comb(m, s):
    if m == 0:
        return [ [] ]
    if s == []:
        return []
    # print([ s[:1] + a for a in comb(m-1, s[1:]) ] + comb(m, s[1:]))
    return [ s[:1] + a for a in comb(m-1, s[1:]) ] + comb(m, s[1:])

x = comb(3, [0,1,2,3,4] )
print(x)



