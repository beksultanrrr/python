l = []
for i in range(5):
    a=int(input())
    l.append(a)
sum=0
for i in range(5):
    if l[i]%2==0:
        sum +=l[i]
print(sum)