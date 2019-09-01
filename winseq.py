n=int(input())
m=1
p=n*n+1
for i in range(n,0,-1):
    for j in range(n-i):
        print("**",end="")
    for j in range(i):
        print(m,end="0")
        m+=1
    for j in range(i-1):
        print(p,end="0")
        p+=1
    print(p)
    p-=2*(i-1)