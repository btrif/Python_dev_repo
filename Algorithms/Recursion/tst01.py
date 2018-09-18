#  Created by Bogdan Trif on 30-06-2018 , 3:16 PM.

L= [1, 4, 9, 16]

def decompose( n, our_lst, answerSoFar=[] ):

    if n ==0 :
        # recursion has finished, print the list
        print(answerSoFar)
        return
    else :
        offset = 0
        for a in our_lst :
            if a <= n :
                answerSoFar.append(a)
                decompose(n-a, our_lst[ offset: ], answerSoFar )
                answerSoFar.pop()   # remove a from the list, so we can try replacing by later items too.

            offset +=1


decompose(13, L)

