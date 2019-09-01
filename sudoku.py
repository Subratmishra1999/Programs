def is_safe(a,i,j,c):
    e=i
    d=j
    i-=i%3
    j-=j%3
    for k in range(9):
        if(a[e][k]==c):
            return False
        if(a[k][d]==c):
            return False
    #print(c,d)
    for k in range(i,i+3):
        for l in range(j,j+3):
     #       print(k,l,i,j)
            if(a[k][l]==c):
                return False
    #print("hiif")
   # print(*a,sep="\n")
    #print()
    return True
def is_empty(a,l):
    for i in range(9):
        for j in range(9):
            if(a[i][j]==0):
                l[0]=i
                l[1]=j
                return True
    return False

def sol(a):
    l=[0,0]
    if(not is_empty(a,l)):
        return True
    else:
        i=l[0]
        j=l[1]
        for k in range(1,10):
            if(is_safe(a,i,j,k)):
                a[i][j]=k
                #print(*a,sep="\n")
                #print()
                if(sol(a)):
                    return True
                a[i][j]=0
    return False



n=int(input())
for i in range(n):
    l=[]
    for j in  range(9):
        a=[int(_) for _ in input().split()]
        l.append(a)
    print(sol(l),*l,sep="\n")

