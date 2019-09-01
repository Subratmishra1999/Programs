
def s():
  global p,q,m,d
  while(True):
    if(p==m):
      d[(p,q)]=1
      return p,q
    elif (p+1,q) in d:
      p+=1
    else:
      d[(p+1,q)]=1
      break
  d[(p+1,q)]=1
  if(p<m):
    return p+1,q
  else:
    return p,q

def n1():
  global p,q,d
  while(True):
    if(p==0):
      d[(p,q)]=1
      return p,q
    elif (p-1,q) in d:
      p=p-1
      d[(p,q)]=1
    else:
      break
  if(p==0):
    d[(p,q)]=1
    return p,q
  else:
    d[(p-1,q)]=1
    return p-1,q

def e():
  global p,q,n,m,d
  while(True):
    if(q==n):
      d[(p,q)]=1
      return p,q
    elif (p,q+1) in d:
      q=q+1
    else:
      d[(p,q+1)]=1
      break
  if (q<n):
    return p,q+1
  else:
    return p,q

def w():
  global p,q,n,m,d
  while(True):
    if(q==0):
      d[(p,q)]=1
      return p,q
    elif (p,q-1) in d:
      q=q-1
    else:
      d[(p,q-1)]=1
      break
  if(q>0):
    return p,q-1
  else:
    return p,q
a=int(input())
for j in range(a):
  n,m,o,p,q=map(int,input().split())
  m-=1
  n=o
  n-=1
  p-=1
  q-=1
  K=input()
  d={(p,q):1}

  for i in K:
    #print(p,q,"now")
    if(i=='S'):
      p,q=s()
    elif(i=='N'):
      p,q=n1()
    elif(i=='E'):
      p,q=e()
    else:
      p,q=w()
  print("Case #{}: {} {}".format(j+1,p+1,q+1))
