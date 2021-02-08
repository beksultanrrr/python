def fun(n):
    if n<1:
        return 0
    else:
        return n+fun(n-2)
n=int(input())
print(fun(n))