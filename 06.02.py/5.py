def f(a,b,c):
    if(a>=b and a>=c):
        return a
    elif (b>=a and b>= c ):
        return b
    return c
m=f(3,8,5)
print(m)