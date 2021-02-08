a=(input())
for i in a:
    if a[0].lower() and a[1:-1].upper() and a[-1].upper():
    
        print(a[0].upper()+a[1:-1].lower()+a[-1].lower())
        break
    if a.lower():
        print(a.upper())
    else:
        print(a)
        break
    