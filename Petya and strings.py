x=input().lower()
y=input().lower()
c=0
for i in range(len(x)):
    x1=ord(x[i])
    y1=ord(y[i])
    if x1>y1:
        c=1
        break
    elif x1<y1:
        c= -1
        break
    else:
        continue
print(c)           
