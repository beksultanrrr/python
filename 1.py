import math
x = float(input())

if -5 >= x >= -9:
    y = (-1)*math.sqrt(4 - (x+7)*2) + 2
elif -4 >= x >= -5:
    y = 2
elif 0 >= x >= -4:
    y = -0.5*x
elif math.pi >= x >= 0:
    y = math.sin(x)
elif 5 >= x >= math.pi:
    y = x - math.pi
print(x, y)