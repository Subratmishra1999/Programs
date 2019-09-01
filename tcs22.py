r1=float(input())
n,m=map(int,input().split())
l=input().split()
ball=len(l)
run=0
for i in l:
    if ord(i)<55:
        run+=int(i)
r2=float(input())
ob=int((ball*r2-6*run)/(r1-r2))
cr=int(r1/6*ob)
cr+=run
c,d=0,0
f,g=0,0
e=0
for i in range(0,len(l),6):
    if(e%2==0):
        if('W' in l[i:i+6]):
            for j in l[i:i+6]:
                if(j=="W"):
                    c=0
                    f=1
                else:
                    c+=int(j)
        else:
            for j in l[i:i+6]:
                c+=int(j)
    else:
        if('W' in l[i:i+6]):
            for j in l[i:i+6]:
                if(j=="W"):
                    d=0
                    g=1
                else:
                    d+=int(j)
        else:
            for j in l[i:i+6]:
                d+=int(j)
    e+=1
if(f==0):
    m+=c
    print(m,c)
    c=m
if(g==0):
    n+=d
    print(n,d)
    d=n
print(cr,c,d)