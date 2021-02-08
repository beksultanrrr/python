l=[100,3513,2420,523]
l1=[]
l2=[]
for i in range(4):
    if l[i]%2==0:
        l1.append(l[i])
    else:
        l2.append(l[i])
print(l1,l2)