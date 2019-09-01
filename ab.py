n=int(input())
k=int(input())
l=[0 for _ in range(k)]
i=0
j=1
while(n>0):
    if(i>0):
        i%=k
    if(n>=j):
        n-=j
        l[i]+=j
    else:
        l[i]+=n
        break
    j+=1
    i+=1
    print(l)
    
print(l)