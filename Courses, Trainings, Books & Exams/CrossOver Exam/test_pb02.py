#  Created by Bogdan Trif on 17-03-2018 , 7:35 PM.

def generate_string(length) :
    from random import randint
    a, b ='<', '>'
    S=''

    for i in range(length):
        r = randint(1, 2)
        if r % 2 ==0 :
            S += a
        else : S+= b
    #     print(r, '    ', S)

    # print(S,'   .<. = ', S.count(a), '     .>. = ',S.count(b) )

    return S #S.count(a), S.count(b)



from random import randint
length = 25
expressions = [ generate_string(11) for i in range(length) ]
maxReplacements = [ randint(0, 5) for i in range(length)  ]

print()
print( len(expressions), expressions)
print( len(maxReplacements), maxReplacements,'\n')





def balancedOrNot(expressions, maxReplacements):
    ''' Remark : Nice problem !
    :param expressions: lst, list of strings
    :param maxReplacements: , int, corresponding to each element in expressions
    :return: list of ints of 0, 1    '''


    assert ( len(expressions) == len(maxReplacements) ),  "The two lists must be of equal length"
    assert (   1<=  len(expressions) <= 10**2    ), " Please make sure that  the expressions length is greater than 1 & not greater than 10.000 "


    def tryToBalance( S, maxR):
        S = S.strip()       # I had some nasty bugs when copy paste and I put this condition !
        # print('\nstring : ', S , type(S), len(S) , S.startswith('<') and S.endswith('>')  )
        assert (   1<=  len(S) <= 10**5    ), " Please put not null strings arguments & not greater than 10.000 "
        assert (   0 <=  maxR <= 10**5    ), " Please put not negative strings arguments & not greater than 10.000 "


        a, b = '<', '>'
        cnta, cntb = S.count(a), S.count(b)
        # print('.'+ a +'. = ' ,cnta ,'      .'+ b +'. = ' ,cntb,  end = ';  ' )

        if S.endswith(a) :  # CASE 0 : No need for further analysis
            # print('CASE 0     .'+ a +'. = ' ,cnta ,'      .'+ b +'. = ' ,cntb,  end = ';  ' )
            return 0

        if cnta > cntb :    # CASE 1 : No need for further analysis as we cannot replace the '<' to balance
            # print('CASE 1     .'+ a +'. = ' ,cnta ,'      .'+ b +'. = ' ,cntb,  end = ';  ' )
            return 0

        if cnta == cntb :               ### CASE 2 : Equal number of '<' and ' >'
            # print('CASE 2     .'+ a +'. = ' ,cnta ,'      .'+ b +'. = ' ,cntb,  end = ';  ' )
            if S.startswith(a) and S.endswith(b) :
                # print('\nthis case of      1     is executed     !!!!  ', S.startswith(a) and S.endswith(b) )
                return 1
            else :
                print('\nthis case of      0     is executed     !!!!  ', S.startswith(a) and S.endswith(b)  )
                return 0

        if cnta < cntb :    ### CASE 3 : Detailed Analysis
            # print('CASE 3     .'+ a +'. = ' ,cnta ,'      .'+ b +'. = ' ,cntb,  end = ';  ' )
            # print()
            if maxR >= cntb-cnta :
                bal, replacements =  0, 0
                for cnt, s in enumerate(S) :
                    if s == b :
                        bal+=1
                        if bal > 0 :
                            bal -= 1
                            replacements +=1

                    if s == a :
                        bal -= 1

                    # print(str(cnt),'.     ',s,'     balance : ', bal ,'      replacements = ', replacements   )

                if bal == 0 and replacements <= maxR:
                    return 1
                else : return 0

            else :
                return 0

        return None     # I used this as a test case to make sure that I do not miss some cases. My tests worked fine !!!



    RES=[]      # To fill list

    for i in range(len(expressions)) :
        t = tryToBalance( expressions[i], maxReplacements[i]  )
        print('         string  :   ' ,expressions[i] ,'      maxR= ', maxReplacements[i] ,'        res = ',  t )
        RES.append(t)

    print('\nRES : ', RES)
    return RES



balancedOrNot( expressions, maxReplacements )