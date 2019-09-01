t=int(input())
for a in range(t):
    n=int(input())
    l=[]
    for i in range(n):
        l.append(input())
    d={}
    n=[]
    d2={}
   # print(l)
    for i in l:
      #  print(d,n,d2)
        if(i not in n):
            c=len(i)-1
            m=0
            p=0
            while(m==0 and c>=0):
                if(len(d2)*2==len(l) or len(d)*2==len(l)):
                    break
                for j in l:
                   # print(d,n,d2,"   as")
                    if j in n:
                        pass
                    if(i==j):
                        pass
                    else:
                        if(len(j)>len(i)):
                            k=len(j)-len(i)
                        else:
                            k=0
                        k+=p
                        if(k>len(j)):
                            m=1
                        if j[k:] not in d2:
                            #print(d,n,d2,"   asdf")
                           # print(i,j[k:],k,"it is i and j")
                            o=i.find(j[k:])
                            if(len(i)-o==len(j[k:])):
                            #    print(o,"it is o")
                                if(o!=-1):
                                    d[i]=j
                                    d2[j[k:]]=0
                                    m=1
                                    n.append(i)
                                    n.append(j)
                                    break
                p+=1
    c=len(d)*2
    print("Case #{}: {}".format(a+1,c))