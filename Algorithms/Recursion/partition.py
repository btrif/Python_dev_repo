#  Created by Bogdan Trif on 09-09-2017 , 9:34 PM.


def partition(number):
    answer = set()
    answer.add((number, ))
    for x in range(1, number):
        for y in partition(number - x):
            answer.add(tuple(sorted((x, ) + y)))
            #print(answer)
    return answer

print(partition(4))
