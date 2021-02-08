d1={1:20,5:40,2:30,7:32}
d2={2:32,3:45,5:23}
d3={}
for i,j in d1.items():
    for x,y in d2.items():
        if j==y:
            d3[x]=i+x
print(d3)
    