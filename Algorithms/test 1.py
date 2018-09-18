

L = [ 1, 4, 9, 16 ]

def decomp_rec( n, L , tmp_lst=[] ):
    if n == 0:
        print(tmp_lst)
    else :
        offset = 0
        for i in range( 0, len(L) ) :
            if n >= L[i] :
                tmp_lst.append( L[i] )
                decomp_rec( n-L[i], L[ offset : ] ,tmp_lst )
                tmp_lst.pop()

            offset+=1



decomp_rec( 13, L )