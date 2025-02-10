a,b=map(int,input().split())
c=[int(i) for i in input().split()]
d=0
e=0
while d<len(c):
    if c[d]<=b:
        e+=1
        d+=1
    else:
        e+=2
        d+=1
print(e)
