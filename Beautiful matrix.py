l=[]
for i in range(5):
    r=[int(i) for i in input().split()]
    l.append(r)
a=0
b=0
for i in range(5):
   for j in range(5):
       if l[i][j]==1:
           a=i
           b=j
c=abs(b-2)+abs(a-2)
print(c)
