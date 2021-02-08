i=0
while i<3:
    a , b=input().split()
    a=int(a)
    b=int(b)
    if (a==0) and (b==0):
        break
    if(a==0) or (b==0):
        continue
    print(a*b)
    i +=1

