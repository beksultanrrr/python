cnt1=0
cnt2=0
n=input()
for i in n:
    if i=="D":
        cnt1 +=1
    if i=="A":
        cnt2 +=1
if cnt1>cnt2:
    print("YES")
else:
    print('No')
print(cnt1,cnt2)

''''
s = input()
cnt1 = 0
cnt2 = 0
for i in range(len(s)):
    if s[i] == "A":
        cnt1+=1
    else:
        cnt2+=1
print(cnt1 if cnt1>cnt2 else cnt2)
'''