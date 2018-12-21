

print('\n############ ALGO 1 - DYNAMIC PROGRAMMING ################')

RNG = 13

n = [1]
def tile_count(x):
    total = n[x-1]
    for i in range(3, x+1):
        if i is x: total += 1
        else: total += n[x-i-1]
    return total

for x in range(1,RNG+1):
    n.append(tile_count(x))
    print(n)

print(n[RNG])


############ ALGO 2 ################
print('\n############ ALGO 2 ################')






############ ALGO 3 ################
print('\n############ ALGO 3 ################')





############ ALGO 4 ################
print('\n############ ALGO 4 ################')






