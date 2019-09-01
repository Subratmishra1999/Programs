n=int(input())
for i in range(n):
    c=0
    m=input().split()
    m=int(m[1])
    s=input()
    s=list(s)
    #print(s)
    for j in range(m):
        l=[int(_) for _ in input().split()]
        k=s[l[0]-1:l[1]]
       # print(k)
        d={}
        for a in k:
            if a not in d:
                d[a]=1
            else:
                d[a]+=1
        b=0
        if(((l[1]-l[0])+1)%2==0):
            for a in d:
                if(d[a]%2!=0):
                    b=2
                    break
            if(b==0):
                c+=1
        else:
            e=0
            for a in d:
                if(d[a]%2!=0 and e!=0):
                    b=2
                    break
                else:
                    e=1
            if(b==0):
                c+=1
    print("Case #{}: {}".format(i+1,c))
