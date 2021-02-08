n=int(input())
s=str(n)
for num in s:
    if s.count('0')>7:
        print('YES')
        break
    elif s.count('1')>7:
        print('YES')
        break
    else:
        print('No')
        break
    

