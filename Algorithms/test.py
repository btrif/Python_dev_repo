import time

t1  = time.time()

coin = [1,2,5,10,20,50,100,200]

def pb031(n, arr):
    last = arr[-1]
    if len(arr) == 1:
        return 1
    return sum(pb031(n-last*i,arr[:-1]) for i in range(n//last+1))

print(pb031(20, coin))

t2  = time.time()
print('\n', ' Completed in  in :', round((t2-t1)*1000,4), 'ms\n')

def coin_change(x, coins, i=0):
    return 1 if x == 0 else 0 if i == len(coins) else\
           sum(coin_change(x - n * coins[i], coins, i+1) for n in range(x // coins[i] + 1))
print(coin_change(20, [20, 10, 5, 2, 1]))
#print(coin(200, [200, 100, 50, 20, 10, 5, 2, 1]))


t1  = time.time()

def coinsum(value):

    coins = [1,2,5,10,20,50,100,200]

    ways = [0] * (value+1)
    ways[0] = 1

    while coins[-1] > value:
        del(coins[-1])

    for i in range(len(coins)):
        for j in range (coins[i],value + 1):
            ways[j] += ways[j - coins[i]]

    print (ways[-1])

coinsum(200)


t2  = time.time()
print('\n', ' Completed in  in :', round((t2-t1)*1000,4), 'ms\n')


total = 200
combinations = [1] + [0]*total
monies = [1,2,5,10,20,50,100,200]

for x in monies:
	for i in range(x,201):
		combinations[i] += combinations[i-x]

print (combinations[total],'\n\n')

f = open('pb018.txt', 'r')
text = f.read()
f.close()
# Initialize and populate triangle
triangle = []
print(text,'        ',type(text),'\n')

for row in text.split('\n'):
    triangle.append(list(map(int, row.split(' '))))         # This maps the strings into ints on the run, SMART TECHNIQUE

for i in range(len(triangle)-2,-1,-1):
    for j in range(0, i+1):
        #print(max(triangle[i+1][j], triangle[i+1][j+1]), end = ' ')
        triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
    print(triangle[i], end=' \n ')

print('\n',triangle[0][0])