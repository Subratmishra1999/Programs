a=int(input())
for _ in range(a):
    n=input().split()
    k=int(n[1])
    n=int(n[0])
    l=[int(i) for i in input().split()]
    m=[int(i) for i in input().split()]
    d=0
    for i in range(n):
        c=l[i]
        e=m[i]
        for j in range(i,n):
            if(c<l[j]):
                c=l[j]
            if(e<m[j]):
                e=m[j]
            if(abs(c-e)<=k):
                d+=1
            else:
                pass
    print("Case #{}: {}".format(_+1, d))
