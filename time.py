'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here


l=[]
def is_attack(i,j):
    global l,n
    for k in range(n):
        if(l[i][k]==1 or l[k][j]==1):
         #   print("hi")
            return True
    for k in range(n):
        for m in range(n):
            if((k+m==i+j) or (k-m==i-j)):
                if(l[k][m]==1):
             #       print("hi")
                    return True
    return False

def sol(n):
    global l
    if n==0:
        return True
    for i in range(N):
        for j in range(N):
            #print(i,j,l)
            if(is_attack(i,j) or l[i][j]==1):
                continue
            else:
                l[i][j]=1
                if(sol(n-1)==True):
                    return True
                else:
                    l[i][j]=0
                #print(l[i])
    return False
    
n=int(input())
N=n
l=[[0]*n for _ in range(n)]
if(sol(n)):
    for i in l:
        print(i)
else:
    print("Not possible")
