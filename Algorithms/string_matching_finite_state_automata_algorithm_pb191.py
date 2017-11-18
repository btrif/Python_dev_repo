
############## STRING MATCHING   -   FINITE STATE MACHINE Algorithm            ###############

#################     Approach ##############
                #                                 First day :
                # _________  |             0A              |           1A             |            2A            |
                #     1L       |              1               |            0              |               0            |
                #     0L       |              1               |            1              |               0            |
                #
                #                                           Next day :
                # __________|  A+B+C+D+E+F     |           1A             |            2A            |
                #     1L       |          D+E+F          |            0              |               0            |
                #     0L       |              1               |            1              |               0            |



def pb191_dynamic_programming(days):

    A , B, C , D, E, F = 1, 0, 0, 1, 1, 0
    for i in range(2, days+1 ):
        tA = A+B+C+D+E+F
        tB = A
        tC = B
        tD = D + E + F
        tE = D
        tF = E
        A, B, C, D, E, F = tA, tB, tC, tD, tE, tF
        S = A+B+C+D+E+F
        print('day: '+str(i)+'   ', A, B, C, D, E, F , S)

    return print('\nAnswer : \t', S)

pb191_dynamic_programming( 30 )