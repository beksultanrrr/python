l=int(input())
cnt=0

for i in range(1,l+1):
    cnt=i*i
    if cnt>l:
        break
    print(cnt)
    