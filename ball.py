a=int(input())
for i in range(a):
    n,m=map(int,input().split())
    c=0
    l=[]
    k=0
    d=0
    for j in range(n):
        l.append(int(input()))
    #print()
    for j in range(n):
        #print(c)
        if(c+l[j]==m or c==m):
            d=1
            break
        elif(c+l[j]<m):
            c+=l[j]
        elif(c+l[j]>m):
            while(c+l[j]>m):
                c-=l[k]
                k+=1
               # print(c,k)
            c+=l[j]
    if(d==1 or c==m):
        print("YES")
    else:
        print("NO",c)
            