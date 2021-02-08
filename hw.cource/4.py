l=int(input())
cnt=1
for i in range(1,l+1):
    if i*i==1:
        print(1)
    if i*i==2:
       cnt=i*i
    else:
        cnt=cnt*2
    if cnt>l:
        break
    print(cnt)