#  Created by Bogdan Trif on 11-11-2017 , 8:03 PM.
import time

print('\n--------------------------SOLUTION 9,  DEPTH FIRST SEARCH, DFS --------------------------')
t1  = time.time()

# ====Fri, 27 Nov 2009, 01:33, loreto, England
# I initially noticed some similarities with Gray Code but hadn't heard of De Bruijn's sequence.
# Still, using a depth-first search I got the answer in 1 second, in Python 3:

N = 5

total = 0
def score(ring):
    global total

    v = 0
    for a in ring: v = 2*v+a
    total += v

def search(seen, ring):
    if len(ring) == 2**N:
        for i in range(1, N):
            a = ring[-i:]+ring[:N-i]
            if tuple(a) in seen: return
            seen |= set([tuple(a)])

        score(ring)
        return

    a = ring[-(N-1):]+[0]
    b = ring[-(N-1):]+[1]

    if tuple(a) not in seen: search(seen|set([tuple(a)]), ring+[0])
    if tuple(b) not in seen: search(seen|set([tuple(b)]), ring+[1])


search(set([tuple([0]*N)]), [0]*N)
print(total)

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


