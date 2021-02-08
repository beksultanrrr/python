list=[1,2,3,3,2,3,4,5,5,5]
a=dict()
for i in list:
    if i not in a:
        a[i]=0
    a[i] +=1
print(a)