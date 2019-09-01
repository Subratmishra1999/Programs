def manageexpense(a,b,n,expense,l):
  c=b/n
  d=l.index(a)
  for i in range(n):
    if(i==d):
      continue
    e=expense[i][d]
    e+=c
    f=expense[d][i]
    #print(e,f,i)
    if(f!=0):
      if(f-e>0):
        expense[i][d]=0
        expense[d][i]=f-e
      elif(f-e<0):
        expense[i][d]=e-f
        expense[d][i]=0
      else:
        expense[i][d]=0
        expense[d][i]=0
    else:
      expense[i][d]+=c


def show(expense,l):
  print(*l)
  for i in range(n):
    print(l[i],*expense[i])

def menu():
  a=int(input("1: Add Expense\n2: Show Expense\n3: Exit Program\n"))
  return a

n=int(input("Enter the no. of people\n"))
l=[]
for i in range(n):
  l.append(input("Enter the name of {} person\n".format(i+1)))
expense=[[0 for i in range(n)] for j in range(n)]
#print(expense)
#3print(*l,sep="\n")
while(True):
  c=menu()
  if(c==3):
    break
  elif(c==1):
    a=input("Who paid\n")
    b=int(input("How much?\n"))
    manageexpense(a,b,n,expense,l)
  else:
    show(expense,l)