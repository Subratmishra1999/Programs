def isprime(n):
    for i in range(2,n//2+1):
        if(n%i==0):
            return False
    return True

n=int(input())
l=[]
for i in range(2,n):
    if(isprime(i)):
        l.append(i)
print(l,len(l))