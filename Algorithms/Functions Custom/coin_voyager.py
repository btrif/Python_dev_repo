#  Created by Bogdan Trif on 15-12-2017 , 7:55 PM.


UNB =     [0.2249, 0.2127, 0.2266, 0.2111, 0.2223, 0.2019, 0.1811, 0.1778, 0.1787, 0.1737,
            0.166, 0.1622, 0.1622, 0.162, 0.1636, 0.1646, 0.1635, 0.1595, 0.1617, 0.1623,
            0.1587, 0.15, 0.15, 0.1497, 0.1533, 0.1533, 0.1571, 0.1571, 0.1589, 0.1589,
            0.1594, 0.1553, 0.1553, 0.1553, 0.1583, 0.1517, 0.1517, 0.1517, 0.1517, 0.1517,
            0.15, 0.1517, 0.1516, 0.1516, 0.1516, 0.1516, 0.1516, 0.1488, 0.1488, 0.1488,
            0.1488, 0.1488, 0.1488, 0.1488, 0.1488, 0.1488, 0.1488, 0.1488, 0.1488, 0.1488  ]


UNB = UNB[::-1]


FAIR = [ 0.1643, 0.1643, 0.1643, 0.1643, 0.1643, 0.1643, 0.1643, 0.1643, 0.1643, 0.1643,
            0.1643, 0.1643, 0.1643, 0.1643, 0.1643, 0.1569, 0.1569, 0.1511, 0.1511, 0.1511,
            0.1551, 0.1551, 0.1551, 0.1551, 0.1551, 0.1551, 0.1462, 0.1498, 0.1472, 0.1485,
            0.1474, 0.1476, 0.1504, 0.1491, 0.1478, 0.1491, 0.148, 0.1478, 0.1476, 0.1463,
            0.1476, 0.1465, 0.1478, 0.14, 0.1416, 0.1416, 0.1416, 0.1416, 0.1416, 0.1416,
            0.1416, 0.1416, 0.1416, 0.1439, 0.1439, 0.1439, 0.1439, 0.1439, 0.1439, 0.1439,
            0.1439, 0.1439, 0.1439, 0.1439, 0.1438, 0.1414, 0.1414, 0.1414, 0.1414, 0.1414,
            0.1414, 0.1414, 0.1414, 0.1414, 0.1414, 0.1414, 0.1414, 0.1414, 0.1414, 0.1414, 0.1368,
            0.1368, 0.1368, 0.1368, 0.1368, 0.1368, 0.1368, 0.1368, 0.1368, 0.1368, 0.14,
            0.14, 0.14, 0.14, 0.14, 0.14, 0.14, 0.14, 0.1441, 0.1448, 0.1448,
            0.1448, 0.1423, 0.1423, 0.1413, 0.1413, 0.1413, 0.1413, 0.1413, 0.1413,
            0.1413, 0.1413, 0.1413, 0.1413, 0.1413, 0.1425, 0.1425, 0.1425, 0.1425, 0.1425 ]

FAIR = FAIR[::-1]


def monotonic_increase(L) : # Very simple function which must work in many programming languages,  O(n)
    for i in range(len(L)-1) :
        if L[i] > L[i+1] :
            return False
    return True

def moving_average( Arr  , step ) :
    ''' :Description: returns False if the average of the array is not continuously increasing
        Returns True if the moving average is continuously increasing.
    :param Arr:     Array to analyze, list
    :param step: step of the Array. Example 10 means it takes 10 values at a time
    :return: True if increasing, False if non increasing
    '''
    B = []
    for i in range(len(Arr)) :

        if i%step == 0 :
            Slice =  Arr[i:i+step]
            avg = sum(Slice)/step
            # print(str(i)+'.      ', Arr[i], '      ' , Slice , '   ;     avg = ',   avg )
            B.append( avg )

    print(B)
    if monotonic_increase(B) :
        return True

    return False

print('\nTesting function moving_average UNB : \t' ,moving_average(UNB , 10),'\n---------' )
print('\nTesting function moving_average  FAIR: \t' ,moving_average(FAIR , 15),'\n----------' )