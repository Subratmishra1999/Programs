m=int(input())
for j in range(m):
    n=int(input())
    l=[]
    for i in range(n):
        k=[int(_) for _ in input().split() ]
        l.append(k)
    l=sorted(l,key=lambda x: (x[1],x[2]),reverse=True)
    c=0
    k=0
    for i in range(len(l)):
        if(l[i][1]-l[i][2]*k>0):
            c+=(l[i][1]-l[i][2]*k)
        k+=l[i][0]
    print("Case #{}: {}".format(j+1,c))
