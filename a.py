from decimal import *
a=input()
a=int(a)
b=int(input())
getcontext().prec=200
a=Decimal(a)
b=Decimal(b)
print(a/b)