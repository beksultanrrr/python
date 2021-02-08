def fun(n):
    if n<0:
        return 0
    else:
        return 1/(2**n+fun(n-1))
n=int(input())
print(fun(n))
