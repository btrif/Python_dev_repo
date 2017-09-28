from math import e
from decimal import *
print(getcontext())
print(Decimal('7.325').quantize(Decimal('1.'), rounding=ROUND_UP))
print(Decimal('7.3259999').quantize(Decimal('.001'), rounding=ROUND_DOWN))

getcontext().prec =103
print(getcontext())

a = Decimal(e)
print(Decimal(e), len(str(Decimal(e)))  )
print(Decimal(2)/6)