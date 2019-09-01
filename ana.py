def check(d,d1):
    for i in d:
        if i in d1:
            if(d[i]!=d1[i]):
                return "NO"
        else:
            return "NO"
    return "YES"

s=input()
e=s
k=int(input())
#print(n)
n=[]
for i in range(k):
    a=input().split()
    n.append(a[0])
    n.append(a[1])
#print(n,s)
#print(n,k)
b=len(s)
c=0
a=""
for i in range(k):
    n1=n[c]
    n2=int(n[c+1])
    c+=2
 #   print(n1,n2,e,a)
    if(n1=="L"):
        #print(s[n2:],s[:n2])
        s=s[n2:]+s[:n2]
        a+=s[0]
        #print(s)
    else:
       # print(s[b-n2:],s[:],"as")
        s=s[b-n2:]+s[:b-n2]
        a+=s[0]
        #print(s)
#print(a)
#print(len(e),len(a),e,a)
d={}
d1={}
for i in range(len(a)):
    if a[i] not in d:
        d[a[i]]=1
    else:
        d[a[i]]+=1
    if e[i] not in d1:
        d1[e[i]]=1
    else:
        d1[e[i]]+=1
if(len(d)==len(d1)):
    c=check(d,d1)
if(c=="YES"):
    print("YES")
else:
    c=0
    m="NO"
    for i in range(len(a),b):
        #print(d1,e[c],d)
        d1[e[c]]-=1
        #print(d1)
        if(d1[e[c]]==0):
            del d1[e[c]]
        if e[i] in d1:
            d1[e[i]]+=1
        else:
            d1[e[i]]=1
        if(len(d)==len(d1)):
                m=check(d,d1)
        if(m=="YES"):
            print("YES")
            break
        c+=1
    if(m!="YES"):
        print("NO")

    