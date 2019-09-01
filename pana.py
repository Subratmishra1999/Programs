def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return False
    return True
def makelist(b,j):
    c=[j,int(b[0]/j)]
    if(b[1]%j==0):
        c=[int(b[0]/j),j]
    k=1
    j=c[1]
    for i in range(1,len(b)):
        c.append(int(b[i]/j))
        k+=1
        j=c[k]
    k=c[:]
    #k.sort()
    k=set(k)
    k=list(k)
    k.sort()
    d={}
    l="A"
    for i in k:
       # print(d)
        d[i]=l
        l=chr(ord(l)+1)
    l=""
    for i in c:
        l+=d[i]
    print(l)
    return True
      
n=int(input())
for i in range(n):
    a=10000
    #a=int(a[0])
    #b=[217,1891,4819,2291,2987,3811,1739,2491,4717,445,65,1079,8383,5353,901,187,649,1003,697,3239,7663,291,123,779,1007,3551,1943,2117,1679,989,3053]
    b=[int(_) for _ in input().split()]
    for j in range(3,a,2):
        if(isprime(j)):
            if(b[0]%j==0):            
                if(makelist(b,j)):
                    break
                else:
                    continue
            else:
                continue