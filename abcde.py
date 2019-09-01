n=int(input())
m=[int(_) for _ in input().split()]
a=input()
l=[int(_) for _ in input().split()]
k=[[] for i in range(len(m))]
c=0
d=[]
g={}
for i in range(len(l)):
    c=0
    for j in range(len(m)-1,-1,-1):
        if(m[j]>=l[i] and len(k[j])<j+1 and (i not in g)):
            k[j].append(l[i])
            d.append(j+1)
            g[i]=1
            c=1
    if(c==0):
        d.append(0)
print(*d)