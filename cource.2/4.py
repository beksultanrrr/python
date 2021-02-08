def fun(a,b):
    if b==0:
        return a
    else:
        return fun(b,a%b)
a=int(input())
b=int(input())
print(fun(a,b))