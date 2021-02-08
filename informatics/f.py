a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    print(a)

if a<b and c<b:
    print(b)

if a<c and b<c:
    print(c)

else:
    if a==b and b==c and c==a:
        print(a) 
    
    else:
        if a==b:
            print(a)
        if b==c:
            print(b)
        if a==c:
            print(c)
        
        