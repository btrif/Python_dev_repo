#  Created by Bogdan Trif on 07-01-2019 , 8:43 PM.
# initialize the accumulator, in this case a list
accumulator = []

for i in range(1,11):
# add to the accumulator, in this case add to the list
    accumulator = accumulator + [i ** 2]

print(accumulator)