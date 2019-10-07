'''list1 = []
list2 = []
number = input("enter the number")
for numbers in number:
    if '0' in numbers:
        list1.append(numbers)
    else:
        list2.append(numbers)

print(list1)
print(list2)

merged_list = list1 + list2
print(*merged_list)



s=input().split(',')
n=input()
c=0
m=[]
for i in range(len(s)):
    c=len(n)
    a=s[i]
    k=""
    for j in range(len(a)):
        b=ord(a[j])
        b+=int(n[c%len(n)])
        c+=1
        if(b>90):
            b=65+(b-90)-1
        k+=chr(b)
    m.append(k)
print(*m)

c=0
n=int(input())
for i in range(n):
    print(" "*i,end=" ")
    for j in range(n,i,-1):
        if i%2==0:
            print("*",end=" ")
    print()
print(" "*(n)+"*")
for i in range(n):
    print(" "*(n-i-1),end=" ")
    for j in range(0,i+1):
        if i%2!=0:

            print("*",end=" ")
    print()   

n=int(input())
print("*"*n+" "+"*"*n)
for i in range(n-2):
    print(" "*(n-1)+"*"+" "+"*")
print(" "*(n//2+1)+"*"*n)
for i in range(n):
    print(" "*n+"*")    

n=int(input())
l=n//2
if(n==1):
    print("*"(n+2))
else:
    c=1
    for i in range(0,l+1):
        print(" "*(l-i)+"*"*c,"*"*c)
        c+=2
    print("*"*(n*3))
    c=n
    for i in range(l,-1,-1):
        print(" "*(l-i)+"*"*c,"*"*c)
        c-=2


n=int(input())
a=2*n
b=a-1
for i in range(1,n+1):
    if(i==n):
        print("#"*n+"* "*(i-1)+"*"+"#"*i)
        continue
    print(" "*(a-1)+"* "*i)
    a-=1
for i in range(n+2):
    print(" "*b+"$")
    

n=int(input())
l=n//2
for i in range(l):
    print(" "*(l-i)+"*"*(l*i+1)) 
print("*"*n)
for i in range(l,0,-1):
    print(" "*(l-i+1)+"*"*(l*i-1))
for i in range(n+2):
    print(" "*l+"*") 


n=int(input())
print("*\n**@")
for i in range(1,n-1):
    print("*"*(n-i-1)+"@"+"*"*(i))
print(" "*(n//2+1)+"@**")
print(" "*(n+1)+"*")

n=int(input())
k=1
print(" "*(n//2)+"*"*(n+2))
for i in range(n//2+1):
    print("*"*n+" "+"*"*k)
    n-=2
    k+=2






n=int(input())
k=3
a=n+2
b=n+2
for i in range(n-1):
    print(" "*a+"*"*b)
    b-=2
    a+=1

print(" "*(n//2+2)+"*"+"_"*n+"*")
a=n//2+1
for i in range(n-1):
    print(" "*a+"*"*k)
    k+=2
    a-=1

n=int(input())
c=1
k=3
a=3+2*(n-1)

for i in range(n):
    e=" "*(a//2)+"*\n"
    print(e*c,end="")
    b="*"*k
    print(" "*(a//2-len(b)//2)+b+"\n")
    c+=1
    k+=2
    '''
n=int(input())
a=1
b=n//2
c=2*(n//2)+1
for i in range(1,n+2,2):
    print(" "*b+"@"*i+" "*c+"@"*i)
    c-=2
    b-=1
b=1
c=3
for i in range(n-2,-1,-2):
    print(" "*b+"@"*i+" "*c+"@"*i)
    c+=2
    b+=1
c-=2
for i in range(1,n+1):
    print(" "*(n//2)+"*"+" "*c+"*")
print(" "*(n//2)+"@"*(n+2))
c=(n//2)+(n+2)//2
for i in range(1,n+1):
    print(" "*c + "*")

for i in range(1,n+2,2):
    print(" "*(c)+"@"*i)
    c-=1
c+=2
for i in range(n-2,-1,-2):
    print(" "*c+"@"*i)
    c+=1
