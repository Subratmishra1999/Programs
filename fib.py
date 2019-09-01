import time
def fib(n):
    if(n<=1):
        return n
    else:
        return fib(n-1)+fib(n-2)
n=int(input())
b=time.time()
a=fib(n)
c=time.time()
c=b-a
print(a,c)