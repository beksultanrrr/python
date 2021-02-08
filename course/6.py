l1=[]
l2=[]
for i in range(5):
    a=int(input())
    b=int(input())
    l1.append(a)
    l2.append(b)
min=l1[0]
miin=l2[0]
for i in range(5):
    if l1[i]<min:
        min=l1[i]
    if l2[i]<miin:
        miin=l2[i]
if min>miin:
   print(miin)

elif min<miin:
    print(min)
else:
    print("они равны")