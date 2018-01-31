#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Thu, 9 Mar 2017, 19:22
#The  Euler Project  https://projecteuler.net
'''
Connectedness of a network      -       Problem 186
Here are the records from a busy telephone system with one million (10**6)  users:

                                RecNr	    Caller	    Called
                                    1	        200007	    100053
                                    2	        600183	    500439
                                    3	        600863	    701497
                                ...	...	...
The telephone number of the caller and the called number in record n are :
Caller(n) = S_(2n-1) and Called(n) = S_2n where S_1,2,3,... come from the "Lagged Fibonacci Generator":

For 1 ≤ k ≤ 55, Sk = [100003 - 200003*k + 300007k**3] (modulo 1000000)
For 56 ≤ k, Sk = [S_(k-24) + S(k-55)] (modulo 1000000)

If Caller(n) = Called(n) then the user is assumed to have miss dialled and the call fails; otherwise the call is successful.

From the start of the records, we say that any pair of users X and Y are friends
if X calls Y or vice-versa. Similarly,
X is a friend of a friend of Z if X is a friend of Y and Y is a friend of Z;
and so on for longer chains.

The Prime Minister's phone number is 524287.
After how many successful calls, not counting misdials,
will 99% of the users (including the PM) be a friend, or a friend of a friend etc., of the Prime Minister?

'''
import time, itertools, zzz
from collections import deque

def Lagged_Fibonacci_Generator_gen():           # EFFICIENT GENERATOR
    '''    For 1 ≤ k ≤ 55, Sk = [100003 - 200003*k + 300007*k**3] (modulo 1000000)
            For 56 ≤ k, Sk = [S_(k-24) + S(k-55)] (modulo 1000000)                      '''
    from collections import deque
    queue_55 = deque()    
    for k in range(1,56) :
        s = (100003 - 200003*k + 300007*k**3) % 1000000
        # print(k, s)        
        queue_55.append(s)        
        yield s
    while True :
        s = (queue_55[-24]+queue_55[-55])%1000000        
        queue_55.append(s)
        queue_55.popleft()
        # print(len(tmp) ,tmp)
        yield s


print('\n---------------- TESTS ---------')

########   NOT MY CODE. But I can Inspire from it
# def generator():
#     queue_55 = deque()
#     queue_24 = deque()
#     for k in range(1, 56):
#         s_k = (100003 - 200003 * k + 300007 * (k ** 3)) % 1000000
#         queue_55.append(s_k)
#         if k >= 32:
#             queue_24.append(s_k)
#         yield s_k
#     while True:
#         s_k = (queue_55.popleft() + queue_24.popleft()) % 1000000
#         queue_55.append(s_k)
#         queue_24.append(s_k)
#         yield s_k
#
# G = generator()
# cnt = 0
# for i in G :
#     print(i , next(G))
#     cnt+=1
#     if cnt ==100 : break
#
#
# graph_list = [set([i]) for i in range(1000000)]
#
# def get_pos_of(i):
#     while isinstance(graph_list[i], int):
#         i = graph_list[i]
#     return i

print('\n---------------- Test to find the call number of PM ---------')

t1  = time.time()

def first_call_number_of_PM() :
    LFG = Lagged_Fibonacci_Generator_gen()
    PMnr  = 524287
    TS = set()              # TS = Tracker SET
    for i in range(1, 2*10**7+1):
        n1, n2 = next(LFG), next(LFG)
        TS.update({n1,n2})
        if ( n1 or n2 ) == PMnr  :       # call Id :  2575194.      n1=  524287         n2=  974071           Total Nrs : 	 994204
            return print('call Id :  '+str(i)+'.      n1= ', n1, '        n2= ', n2, '          Total Nrs : \t', len(TS) )

# first_call_number_of_PM()

t2  = time.time()
print('\nCompleted in :', round((t2-t1), 6), 's\n\n')

print('\n--------------------------TESTS------------------------------')
t1  = time.time()

def first_attempt() :
    LFG = Lagged_Fibonacci_Generator_gen()
    PMnr , PMnr_id = 524287, 33.33
    PMnr_conn = 0
    NET = []
    TS = set()              # TS = Tracker SET
    for i in itertools.count(1) :
        # if i == 564 : break                   # Controller over the infinite loop
        n1, n2 = next(LFG), next(LFG)

        # CASE 0 - Miss dialled
        if n1 == n2 : continue

        #  CASE 1       -   # FIRST NUMBER - DIALLER, Second not in NET
        if ( n1 in TS ) and (n2 not in TS) :
            for j in range(len(NET)) :
                if n1 in NET[j] :
                    NET[j].add(n2)
                    break

        #  CASE 2       -   # Both are already in Network
        if (n1 in TS) and (n2 in TS ) :
            m1, m2 = None, None
            for j in range(len(NET)) :
                if n1 in NET[j] : m1 = j
                if n2 in NET[j] : m2 = j
                if (m1 and m2) != None : break
            tmp_set = NET[m1].union(NET[m2])

            if m1 > m2 :   NET.pop(m1) ;   NET.pop(m2)
            if m1 < m2 :   NET.pop(m2)  ;  NET.pop(m1)
            if PMnr in tmp_set :                     # We assure that the PM_nr_id    IS NOT changed        !!!
                NET.insert(tmp_set)
                print(len(tmp_set),'         ', tmp_set  )
            else : NET.append(tmp_set)

            # print(len(tmp_set),'\t\t\t', tmp_set)

        #  CASE 3       -       # SECOND NUMBER - CALLED, First not in NET
        if ( n2 in TS ) and ( n1 not in TS ) :
            for j in range(len(NET)) :
                if n2 in NET[j] :
                    NET[j].add(n1)
                    break

        #  CASE 4           # Both numbers are NOT in TS ( Tracker Set )
        if (n1 not in TS) and (n2 not in TS ) :
            NET.append({ n1,n2 } )

        TS.update({n1, n2})

        # SPECIAL CASE - Prime Minister
        if PMnr in TS :             # PRIME MINISTER Connections handle
            if PMnr_id != 0 :      # We move the set of the Prime Minister to the 0 index in the list
                for j in range(len(NET)) :
                    if PMnr in NET[j] :
                        A = NET[j]
                        NET.pop(j)
                        NET.insert(A )
                        PMnr_id = 0
                        print('\n++++++  ', NET[0], '   Total phone numbers : ',len(TS),'  ++++++' )
                        break
            elif PMnr_id == 0 :
                PMnr_conn = len(NET[0])
        if i%10**4 == 0 :
            print('call Id :  '+str(i)+'.     Dialler :', n1, '       Called : ', n2, '      Total Nrs : \t', len(TS) , '      Groups : ', len(NET) , '      fragmentation :\t', round( len(NET)*2/len(TS) ,6), '\t\t', len(TS)-2*len(NET ) )

        # print(len(NET), NET)


        if PMnr_conn >= ( 99 * len(TS) )/100 :
            return print( '\nCalls : \t', i, '\t\t PM conn : \t', PMnr_conn, '    Total nrs :   ', len(TS) )





t2  = time.time()
print('\nCompleted in :', round((t2-t1)/60,6), 'min\n\n')



 ############ UNDERSTANDING THE PROBLEM #############
# It's 99% of the one million users. The list of calls is infinite.
# You're asked how much of that infinite list you need to look at before 99% ' \
# of the users are connected to the PM (either directly or indirectly).
#
# For example, suppose there are five users, and the calls go
#
# CODE: SELECT ALL
# (misdial) 4,4
# 1: 1,4
# 2: 2,4
# (misdial) 3,3
# (misdial) 1,1
# 3: 5,4
# 4: 3,2
# (misdial): 2,2
# 5: 3,4
#
# After the first two successful calls, user 5 is still not connected to anyone.
# After the third, they are connected to users 4 (directly, because of call 3),
# 1 (because 1 is connected to 4 by call 1),
# 2 (because 2 is connected to 4 by call 2),
# and 5 (because 4 is a friend of 5, and 5 is a friend of 4,
# that makes 5 a friend of a friend of 5).
# At this point, user 5 is connected to 4 out of the 5 users, which is 80%.
#
# If we were asked how many successful calls it took for user 5 to be connected to 80% of the users, the answer would be 3.


print('\n==========  My FIRST SOLUTION, With Help  , 30 sec ===============\n')
t1  = time.time()

# ============    @ 2017-03-09, 19:26  ===============
#Couldn't have done it without OBVIOUS HELP from the internet !!! In effect my solution
# would take 1 day to finish and the response would have been wrong as I did not took into account
# correctly the 1.000.000 users comparison and I would have compared with the numbers dialed.async
# But at least I learnt something very important about sets and some nice tricks like the get_position_of
# deque and so on. It this is more important !

def get_position_of( list_of_sets , b):
    while isinstance( list_of_sets[b] , int ) :
        b = list_of_sets[b]
    return b

def calls_number_solution() :
    LFG = Lagged_Fibonacci_Generator_gen()
    PMnr = 524287
    calls = 0
    NET = [ set([i]) for i in range( 10**6) ]

    TS = set()              # TS = Tracker SET
    for i in itertools.count(1) :
        # if i == 15938 : break                   # Controller over the infinite loop
        # if i == 15 : break                   # Controller over the infinite loop
        n1, n2 = next(LFG), next(LFG)
        if n1 == n2 : continue
        calls +=1
        TS.add(n1); TS.add(n2)
        pos1 = get_position_of(NET, n1)
        pos2 = get_position_of(NET, n2)

        if pos1 != pos2 :
            to_put_into = min(pos1, pos2)
            to_remove = max(pos1, pos2)
            NET[to_put_into] |= NET[to_remove]
            NET[to_remove] = to_put_into

        if i%10**5 == 0 :
            print('call Id :  '+str(i)+'.     Dialler :', n1, '       Called : ', n2, '    positions :', pos1, pos2 ,'    Total Nrs : \t', len(TS) ,'    Calls :', calls )
            # print('       ' ,NET[187853: 187857],'    ' ,NET[ 909800:909805],'       ' ,NET[150341:150345])

        PMnr_set_len = len(NET[get_position_of(NET,  PMnr)]  )
        if PMnr_set_len >= 990000 :
            return print( '\nCalls : \t', calls , '\t\t PM conn : \t', PMnr_set_len, '    Total nrs :   ', len(TS) )


calls_number_solution()         #       Calls : 	 2325629 , PM conn : 	 990000     Total nrs :    990458



t2  = time.time()
print('\nCompleted in :', round((t2-t1), 6), 's\n\n')
# zzz.Star_Wars()

print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  1 min , Union Find data structure with path compression --------------------------')
t1  = time.time()

# ==== Sat, 4 Jun 2016, 05:55, will.fiset, Canada
# Here is my solution in Python3 using pypy, it runs in 2seconds using a Union Find data structure with path compression!


class UnionFind (object):

  def __init__(self, n):
    self.n = n
    self.id = [i for i in range(n)]
    self.sz = [1 for _ in range(n)]

  def find(self, p):
    root = p
    while (root != self.id[root]):
      root = self.id[root]
    while(p != root): # Compress
      _next = self.id[p]
      self.id[p] = root
      p = _next
    return root

  def connected(self, p, q):
    return self.find(p) == self.find(q)

  def getSize(self, p):
    return self.sz[self.find(p)]

  def union(self, p, q):
    root1 = self.find(p)
    root2 = self.find(q)
    if root1 == root2: return
    if self.sz[root1] == self.sz[root2]:
      self.sz[root2] += self.sz[root1]
      self.id[root1] = root2
    else:
      self.sz[root1] += self.sz[root2]
      self.id[root2] = root1

MOD = 1000000
PRIME_MINISTER_NUMBER = 524287
THRESHOLD = 990000

people = set()
uf = UnionFind(MOD+1)
S = [0] # One Based, thus the zero placeholder

def pmHasEnoughFriends( uf ):

  prime_minister_friends = uf.getSize( PRIME_MINISTER_NUMBER )
  numPeople = len(people)
  if prime_minister_friends >= THRESHOLD:
    return True
  return False


def solution_1():
    k = 1
    successful_calls = 0
    caller, called = 0, 0
    while k <= 55:

        phone_number = (100003 - 200003*k + 300007*k*k*k) % MOD
        people.add(phone_number)
        S.append(phone_number)

        if k % 2 == 0:
            called = phone_number
        if caller != called:
            uf.union(caller, called)
            successful_calls += 1
        else:
            caller = phone_number

        k += 1

    while True: # K ≥ 56

        phone_number = (S[k - 24] + S[k - 55]) % MOD
        S.append(phone_number)

        if k % 2 == 0:
            called = phone_number
        if caller != called:
            uf.union(caller, called)
            successful_calls += 1
            if pmHasEnoughFriends(uf): break
        else:
            caller = phone_number

        k += 1

    return print ('successful_calls : \t',successful_calls)

# solution_1()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------- SOLUTION 2,  20 sec ,union-find algorithm from Sedgewick  book--------------------')
t1  = time.time()

# ==== Sat, 3 Oct 2015, 01:11, anumoshsad, Bancgladesh
# Used union-find algorithm from Sedgewick's book. First stored the values of sequences upto 1 million
# terms which needs time and memory. Then just run the loop until prime-minister has 99% friends.

class WeightedQuickUnion:
	def __init__(self,N):
		self.count = N
		self.parent = [i for i in range(N)]
		self.size = [1 for i in range(N)]
	def find(self,p):
		root = p
		while root != self.parent[root]:
			root = self.parent[root]
		return root
	def connected(self,p,q):
		return self.find(p)==self.find(q)
	def union(self,p,q):
		if p==q:return
		else:
			rootP,rootQ = self.find(p),self.find(q)
			if rootP==rootQ : return
			elif self.size[rootP]<self.size[rootQ]:
				self.parent[rootP]=rootQ
				self.size[rootQ]+=self.size[rootP]
			else:
				self.parent[rootQ]=rootP
				self.size[rootP]+=self.size[rootQ]
			self.count-=1
def pe186():

	seq=[0]
	for k in range(1,56):
		seq.append((100003 - 200003*k + 300007*k**3)%1000000)
	for k in range(56,10000000):
		seq.append((seq[k-24]+seq[k-55])%1000000)
	x = WeightedQuickUnion(1000001)
	res = 0
	for i in range(len(seq)//2):
		a, b = seq[2*i+1],seq[2*i+2]
		if a!=b:
			res+=1
			x.union(a,b)
			if x.size[x.find(524287)]==990000:
				print(res)

				break

# pe186()

t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')

print('\n--------------------------SOLUTION 3,  10 sec  --------------------------')
t1  = time.time()

# ==== Sat, 4 Jan 2014, 00:42, bobrovsky.serj, Russia
# Elegant, concise and pythonic. Without disjoint-set.

def euler186():
    l = [(300007 * i ** 3 - 200003 * i + 100003) % 1000000 for i in range(1, 56)]
    fr = [[i] for i in range(1000000)]
    calls = k = v = 0

    while len(fr[524287]) < 990000:
        for i in range(2):
            u, v, l[k], k = v, l[k], (l[k] + l[k - 24]) % 1000000, (k + 1) % 55

        if u != v:
            calls += 1
            ufr, vfr = fr[u], fr[v]

            if ufr is not vfr:
                if len(ufr) < len(vfr):
                    ufr, vfr = vfr, ufr
                ufr.extend(vfr)
                for i in vfr:
                    fr[i] = ufr
    return calls


# print(euler186())

t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')

print('\n--------------------------SOLUTION 4,  35 sec  --------------------------')
t1  = time.time()

# ==== Mon, 15 Dec 2014, 07:35, wakkadojo, USA
# I'm shocked my python code took so long. Well, at least I like the structure of the program.
# I'm sure I could have tweaked it to speed it up, or just re-implemented in C to get the standard 150x speedup.

class network:
    def __init__ (self):
        self.parents = [ i for i in range (1000000) ]
        self.sizes = [ 1 for _ in range (1000000) ]
        self.pm_number = 524287
    def find (self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find (self.parents[x])
        return self.parents[x]
    def size (self, x):
        return self.sizes [self.find (x)]
    def join (self, x, y):
        xr, yr = self.find (x), self.find (y)
        if xr != yr:
            self.parents[yr], new_size = xr, self.size (xr) + self.size (yr)
            self.sizes[xr] = self.sizes[yr] = new_size

def calls ():
    l1, l2, n, m = 55, 24, 0, 1000000
    r = [ (100003 - 200003*k + 300007*k**3) % m for k in range (1, l1+1) ]
    while True:
        yield r[n % l1]
        r[n % l1] = (r[(n-l2)%l1] + r[n % l1]) % m
        n += 1

def solution_4() :
    n, c = network (), calls ()
    num_calls = 0
    while n.size (n.pm_number) < 990000:
        n1, n2 = next (c), next (c)
        if n1 != n2:
            num_calls += 1
            n.join (n1, n2)
    return print (num_calls)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5,  48 sec , Union Find  --------------------------')
t1  = time.time()

# ===== Sat, 11 Jul 2015, 00:04, Arancaytar, Germany
# A pure data structure problem for a change. Union Find to the rescue! :D
# (38 seconds; I suspect something can be shaved off there but there's no way around looping over 2 million times.)

from collections import deque

def initfib(a, b):
  return deque(((100003 - 200003*k + 300007*k**3) % 1000000) for k in range(a,b))

def lfib():
  q1 = initfib(1,56-24)
  q2 = initfib(56-24,56)
  while True:
    a, b = q1.popleft(), q2.popleft()
    q1.append(b)
    q2.append((a+b) % 1000000)
    yield a

def chunks(k, z):
  while True:
    a = []
    for i in range(k):
      a.append(next(z))
    yield tuple(a)

class unionfind:
  def __init__(self, n):
    self.x = list(range(n))
    self.sizes = [1]*n

  def find(self, i):
    if self.x[i] != i:
      self.x[i] = self.find(self.x[i])
      self.sizes[i] = self.sizes[self.x[i]]
    return self.x[i]

  def size(self, i):
    return self.sizes[self.find(i)]

  def unite(self, a, b):
    a, b = min(a,b), max(a,b)
    a, b = self.find(a), self.find(b)
    if a != b:
      self.sizes[a] += self.sizes[b]
    self.x[b] = a

def e186():
  friends = unionfind(1000000)
  calls = chunks(2, lfib())
  ncalls = 0
  while friends.size(524287) < 990000:
    a, b = next(calls)
    if a != b:
      ncalls += 1
      friends.unite(a,b)
  return ncalls

# print(e186())

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,   21 sec--------------------------')
t1  = time.time()

# ====Thu, 15 Jan 2009, 18:12, tolstopuz, Russia

def f():
    s = 55 * [0]
    for k in range(55):
        s[k] = (100003 - 200003 * (k + 1) + 300007 * (k + 1) ** 3) % 1000000
        yield s[k]
    while True:
        s[:-1], s[-1] = s[1:], (s[-24] + s[-55]) % 1000000
        yield s[-1]

s = [[None, 1] for i in range(1000000)]

def root(x):
    while s[x][0] != None:
        x = s[x][0]
    return x

def solution_6():
    c = 0
    n = 524287
    m = 0

    for x, y in zip(*[iter(f())]*2):
        if x != y:
            c += 1
            rx, ry = root(x), root(y)
            if s[ry][1] > s[rx][1]:
                rx, ry = ry, rx
            if rx != ry:
                if ry == n:
                    n = rx
                s[ry][0] = rx
                s[rx][1] += s[ry][1]
                m += 1
                if s[n][1] >= 990000:
                    print(c)
                    break

solution_6()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

