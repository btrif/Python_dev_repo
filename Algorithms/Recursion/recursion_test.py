def dragon(n):
    pos= [0,1]
    if n == 1 :
        return [0,1]
    else :
        pos = [ -pos[1], pos[0] ]

        return list(map(2 .__mul__, dragon(n//2) ))


print( dragon(256) )