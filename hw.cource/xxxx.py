a=str(input())
small=0
cap=0
for i in a:
    if 'a' <= i <= 'z':
         small += 1       
    elif 'A' <= i <= 'Z':
                cap += 1
    else:
                pass
print(small,cap)
if small>cap:
    print(a.lower())
else:
    print(a.upper())