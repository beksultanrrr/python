#list 
l  = [] #list
for i in range(3):
    a = int(input())
    l.append(a)
max = l[0]
for i in range(1, 3):
    if l[i]>max:
        max = l[i]
    else:
        pass
print(max)