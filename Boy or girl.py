x=input()
b=list(x)
l=[]
for i in range(len(b)):
    if b[i] in l:
        continue 
    else:
        l.append(b[i])
if len(l)%2==0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')           
