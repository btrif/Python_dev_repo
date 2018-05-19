#  Created by Bogdan Trif on 11-01-2018 , 12:24 PM.

# Number format from scientific notation into float, decimal
from decimal import Decimal

n = 0.00001357
print(n)

# Convert to float :
print( format(n, 'f'))
print( format(n, '.8f'))

print('\n---------------------String input as a number -------------------')
# If we have a number as a string :
string_number = '8205.72'
print('string_number = ', string_number, type(string_number) )
float_nr = float(string_number)
print('float_number = ', float_nr, type(float_nr) )




print('\n-------------- Changing time formats from epoch to custom date time ---------------')
# Actual date and time in
import time
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

from datetime import datetime

print( str(datetime.now( )))
print( datetime.now().strftime('%Y-%m-%d %H:%M:%S') )


print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1517341768)))

print('\n ---------------- Convert from a specific date/time format to epoch time : -----------')
hiredate= '2018-01-30 21:49:28'
pattern = '%Y-%m-%d %H:%M:%S'
epoch = int(time.mktime(time.strptime(hiredate, pattern)))
print(' epoch : ',epoch )


print('\n----------converting custom time formats , BITTREX (SIO Format )-----------')

import datetime


def convert_time_UTC_bittrex_format_to_local(bittrex_time):
    bittrex_time = bittrex_time.split('.')[0]
    bt = datetime.datetime.strptime( bittrex_time, "%Y-%m-%dT%H:%M:%S")
    local_epoch = time.mktime(bt.timetuple())- time.timezone
#     print('local epoch :', local_epoch)
    local_time_standard_form = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(local_epoch) )
    print( 'local_time_standard_form :', local_time_standard_form  )
    return local_time_standard_form

convert_time_UTC_bittrex_format_to_local('2018-03-23T08:45:03.71')


def convert_time_bittrex_format_to_epoch(bittrex_time):
    bittrex_time = bittrex_time.split('.')[0]
    bt = datetime.datetime.strptime( bittrex_time, "%Y-%m-%dT%H:%M:%S")
    # bt = datetime.datetime.strptime( bittrex_time, "%Y-%m-%dT%H:%M:%S.%f")
    # print(bt)
    return time.mktime(bt.timetuple())

def convert_utc_time_to_epoch():
    ut = datetime.datetime.utcnow()
    # print(ut)
    return time.mktime(ut.timetuple())

convert_utc_time_to_epoch()

def convert_epoch_to_standard(epoch):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch))

print('custom time to epoch : ', convert_time_bittrex_format_to_epoch('2018-03-20T09:14:41.83') )
print('convert_utc_time_to_epoch : ', convert_utc_time_to_epoch() )

print('\n-----------------epoch time -----------------')
print('epoch time : ', time.time() )

print('\n-----------------Universal Time UTC, Local time -----------------')
print( datetime.datetime.utcnow())
print( datetime.datetime.now() )

print( datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p") )

# ISO Format :
print( datetime.datetime.utcnow().isoformat() )

print('\nYou can use these in variables for calculations and printing without conversions.')
ts = datetime.datetime.utcnow()
tf = datetime.datetime.now()
te = tf - ts
print(ts)
print(tf)
print(te ,   tf> ts  )

print('\n ----- Get the timezone shift ----------' )
import datetime
def get_timezone_diff():
    ''' This function is not affected by daylight time savings changes on Mars & October
        returns in seconds. Example: 3600, 7200, 10800, ...'''
    utc, local = datetime.datetime.utcnow(), datetime.datetime.today()
    delta = local - utc
#     print('utc time : ',utc, '     local time : ',local)
#     print( 'Timeshift in seconds : ' , delta.total_seconds() )
    return int(delta.total_seconds())


get_timezone_diff()

