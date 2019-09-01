d={}
def count(i,j):
    global d
    c=0
    while(True):
        if(i,j) in d:
            c+=d[(i,j)]
            break
        a=min(i,j)
        if(i>j):
            i-=a
            c+=1
        elif(j>i):
            j-=a
            c+=1
        else:
            i=0
            j=0
            c+=1
            break
    return c
p=int(input())
q=int(input())
r=int(input())
s=int(input())
c=0
for i in range(p,q+1):
    for j in range(r,s+1):
        d[(i,j)]=count(i,j)
        c+=d[(i,j)]
print(c)