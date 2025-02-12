x=int(input())
l=[]
d=0
for i in range(x):
    a=[int(i) for i in input().split()]
    b=0
    for i in range(len(a)):
        if a[i]==1:
            b+=1
        else:
            continue
    l.append(b)        
for i in l:
    if i >1:
        d+=1
print(d)        
