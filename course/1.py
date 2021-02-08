l=[]
for i in range(4):
    a=int(input())
    l.append(a)
sum=0
for i in range(4):
    sum +=l[i]
print(sum)
#2варинат 
for i in l:
    sum +=i