def fun(n):
    if n<=1:
        return 1
    else:
        return fun(n-1)+fun(n-2)
n=int(input())
for i in range(n):
    print(fun(i))