############    ALGO 1 ################

# from time import time;t=time();
# L=21;
# paths=[[]]*L;
# mins=[10]*L;
# mins[0]=0;
# paths[2]=[[2,1]];
# mins[1]=0;mins[2]=1;
# for i in range(2,L):
#     for x in paths[i]:
#         for j in x :
#             n=i+j;
#             if n<L :
#                 if mins[n]>mins[i]+1:
#                     mins[n]=mins[i]+1;
#                     print(mins)
#                     paths[n]=[[n]+x];
#                     print(paths)
#                 elif mins[n]==mins[i]+1:
#                     paths[n]+=[[n]+x]
#     print('---------')
# sol=sum(mins)
# t=1000*(time()-t);
# print ("the answer is %d, this took %d ms" % (sol,t))


############ ALGO 2 ################

#   via RECURSION

def euler_122(limit=200):
    m = [0]+[i for i in range(limit)]
    def explore_node(current, exps):
        steps = len(exps)
        for e in exps:
            candidate = current+e
            if candidate>limit or steps>m[candidate]: continue
            m[candidate] = steps
            explore_node(candidate,[candidate]+exps)
    explore_node(1,[1])
    return sum(m)

# euler_122()





############ ALGO 3 ################
print('\n############ ALGO 3 ################')

import time

start = time.time()

N = 20
n = set(range(1, N + 1))
entire = {1}
chains = {1: [[1]]}
current_level = chains.keys()
while not n <= entire:
    next_level = dict()
    for k in current_level:
        for j in chains[k]:
            newlst = [i + k for i in j if i + k not in entire]
            print(newlst)
            for m in newlst:
                try:
                    next_level[m].append(j.copy() + [m])
                    print(next_level)
                except KeyError:
                    next_level[m] = [j.copy() + [m]]
    for j in next_level:
            chains[j] = next_level[j].copy()
    current_level = next_level.keys()
    entire |= set(current_level)

print(sum([min(map(len, chains[i])) - 1 for i in range(1, N + 1)]))

elapsed = time.time() - start
if elapsed < 1:
    elapsed *= 1000
    text = "milliseconds"
else:
    text = "seconds"
print("Program took:", elapsed, text)





############ ALGO 4 ################
print('\n############ ALGO 4 ################')
limit = 200
cache = {(1,1):[1]}

for n in range(2,limit+1):
  for a in range(n//2+n%2,n):
    if (a,n-a) in cache:
      cache[(n,a)] = [n] + cache[(a,n-a)]
      for x in cache[(n,a)]:
        if (n,x) not in cache or len(cache[n,a]) < len(cache[(n,x)]):
          cache[(n,x)] = cache[(n,a)]

  # print n,len(cache[(n,1)])-1,cache[(n,1)]    # print shortest exponentiation for each n here

sm = sum([len(cache[(x,x)])-1 for x in range(2,limit+1)])
print ("Result",sm)





