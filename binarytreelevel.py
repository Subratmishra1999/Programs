'''Program to print the level of each node in a binary tree having distinct node values'''


class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 

def insert(root,node): 
    if root is None: 
        root = node 
    else: 
        if root.val < node.val: 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node) 

def findlevel(a,c,d):
    d[a.val]=c
    if a.left is None:
        pass
    else:
        findlevel(a.left,c+1,d)
    if a.right is None:
        pass
    else:
        findlevel(a.right,c+1,d)
    


n=int(input())
l=[int(_) for _ in input().split()]
a=Node(l[0])
for i in range(1,n):
    insert(a,Node(l[i]))
d={}
findlevel(a,1,d)
m=[]
for i in l:
    m.append(d[i])
print(*m)

