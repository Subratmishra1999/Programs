'''n,m=map(int,input().split())
k=2**m-1
c=0
for i in range(n):
    a=input()
    d="0b"
    for i in a:
        if(i!=" "):
            d+=i
    d=int(d,2)
    #print(d,"d")
    c+=max(d,k-d)
    #print(d)
print(c)


c=1
for i in range(1,300):
    c*=i
print(c)
'''
a=int(input())
for _ in range(a):
    n,m=map(int,input().split())
    d={i:0 for i in range(1,n+1)}
    e=dict(d)
    for i in range(m):
        g,h=map(int,input().split())
        


