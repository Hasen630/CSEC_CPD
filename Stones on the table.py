x=int(input())
y=input()
n=list(y)
a=0
for i in range(len(n)-1):
    if n[i]==n[i+1]:
         a+=1
print(a)
