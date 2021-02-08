a=str(input())
for i in a:
    if a[0].lower():
        print(a[0].upper()+a[1:-1]+a[-1])
        break
    else:
        print(a)
    