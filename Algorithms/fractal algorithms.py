############ DRAGON HEIGHWAY

def dragonpos(n) :
    c = [0,1]
    length = 1
    while length < n :
        c = [ c[0] + c[1], c[1] - c[0] ]
        length*=2

    if length == n :
        return c

    m = length-n
    c2 = dragonpos(m)
    c2 = [ -c2[1], c2[0] ]

    print(c, length, n, m)

    return [ c[0]+c2[0], c[1]+c2[1] ]

print( '\ndragonpos : ',dragonpos(5) )

print('\n-------------- The Construction of the algorithm ------------------')
print('\n--------------- STEP 1 - BUILD THE MAIN LOOP------------------')
########## STEP 1 - BUILD THE MAIN LOOP ALGORITHM    ###########
# Build the main loop, the loop which is computing the main position calculations.
# Here these are the powers of 2 :  1, 2, 4, 8, 16, 32, ....
# Assure yourself that FIRST this is working properly

# We start at the position (0,1) after one step:
# We use only standard step sizes of powers of 2 :
n=128
pos = [0,1]
step = 1
while step < n :
    step*=2
    pos = [ pos[0] + pos[1], pos[1] - pos[0] ]
    print('step :  ',step,'     position:     ' ,pos)
print()

print('\n--------------- STEP 2 -  Introducing RECURSION  ------------------')
########## STEP 2 - Introducing RECURSION       #############
# After having correctly generated all the powers of 2, we can now
# tackle with any number by decomposing it in powers of two and then adding / substracting
# the parts together. Here we will need recursion and recursion is much more handy than iteration
# So we must take the above loop and integrate it into a recursion function which we'll call dragon

def dragon(n) :
    pos = [0,1]
    step = 1
    while step < n :
        step*=2
        pos = [ pos[0] + pos[1], pos[1] - pos[0] ]
        print('step :  ',step,'     position:     ' ,pos)
    # If this is missing ==> Infinite loop
    if step == n :
        return pos

    diff = step - n
    # Here we make the recursive call which calculates the smaller steps
    d = dragon(diff)
    print( diff, d )
    # We rotate counterclockwise because we must count for the smaller parts
    # which are rotated clockwise already
    d = [ -d[1], d[0] ]

    final_pos = [ pos[0]+d[0], pos[1]+d[1]   ]
    return final_pos

n = 80
print('\nPosition after ',n ,' steps is :   ' ,dragon(n) )

print('\n--------------- STEP 3 -  Implementing MEMOIZATION  ------------------')
########## STEP 2 - Implementing MEMOIZATION       #############
# As we can see above if we print the results in the while loop we have many times
# that the recursive call is calculating the same step numbers. For large computations this
# really slows down the whole calculation. The solution is to implement MEMOIZATION.
# Basically we keep track of the already calculated values and we simply do this by using a
# dictionary as the dictionary is hashed object and is very fast.
# But here it is a little more difficult and not so useful because
# there are not so many recursive calls. It is more difficult because the value n that
# we search is different that the one in the dictionary. So we must choose the closest value
import time
t1  = time.time()


D = { 1 : [0,1] }
def dragonM(n) :
    ''':Description: Dragon with MEMOIZATION      '''
    global D
    pos = [0,1]
    step = 1
    if n in D :  return D[n]
    if n not in D:
        while step < n :
            step*=2
            pos = [ pos[0] + pos[1], pos[1] - pos[0] ]
            D[step] = pos
            print('step :  ',step,'     position:     ' ,pos)
    if step == n :
        return pos

    diff = step - n
    # Here we make the recursive call which calculates the smaller steps
    d = dragonM(diff)
    print( diff, d )
    # We rotate counterclockwise because we must count for the smaller parts
    # which are rotated clockwise already
    d = [ -d[1], d[0] ]

    final_pos = [ pos[0]+d[0], pos[1]+d[1]   ]
    print(D)
    return final_pos

n = 10**12
res = dragonM(n)                                    # Answer :      139776963904
print('\nPosition after ',n ,' steps is :   ' ,res, '\t', ''.join([str(i) for i in res])  )

t2  = time.time()
print('\nCompleted in :', round((t2-t1), 6), 's\n\n')


#################################