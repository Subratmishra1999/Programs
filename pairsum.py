# cook your dish here
t=input()
t=int(t)
for i in range(t):
    n=input().split()
    k=int(n[1])
    n=int(n[0])
    d={}
    a=[int(_) for _ in input().split()]
    for j in range(n):
        if a[j] in d:
            d[a[j]]+=1
        else:
            d[a[j]]=1
    c=False
    print(d)
    for j in d:
        print(j,k-d[j])
        if(j!=k-d[j]):
            if (k-d[j]) in d:
                c=True
                break
        else:
            if(d[j]>1):
                c=True
                break
    if(c==True):
        print("Yes")
    else:
        print("No")
    