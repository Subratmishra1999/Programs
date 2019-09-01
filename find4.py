n=int(input())
for i in range(n):
    a=input()
    s=''
    for j in range(len(a)):
        if(a[j]=='4'):
            s+='1'
        else:
            s+='0'
    a=int(a)
    s=int(s)
    b=a-s
    print("Case #{}: {} {}".format(i+1, b, s))
