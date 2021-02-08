a=int(input())
b=int(input())
for i in range(a,b+1):
    if a<b:
     if i*i>b:
        break
     else:
        print(i*i)