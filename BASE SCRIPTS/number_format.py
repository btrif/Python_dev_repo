#  Created by Bogdan Trif on 11-01-2018 , 12:24 PM.

# Number format from scientific notation into float, decimal
from decimal import Decimal

n = 0.00001357
print(n)

# Convert to float :
print( format(n, 'f'))
print( format(n, '.8f'))

print('-----------------------------')
# Actual date and time in
import time
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

from datetime import datetime

print( str(datetime.now()))
print( datetime.now().strftime('%Y-%m-%d %H:%M:%S') )


print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1517341768)))

print('\n ---------------- Convert from a specific date/time format to epoch time : -----------')
hiredate= '2018-01-30 21:49:28'
pattern = '%Y-%m-%d %H:%M:%S'
epoch = int(time.mktime(time.strptime(hiredate, pattern)))
print(' epoch : ',epoch )