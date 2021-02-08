
for i in range(3):
    a=int(input())
    l.append(a)

for i in range(3):
    l[i] *=l[i]
l.sort()
print(l)