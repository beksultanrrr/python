s=set()
s2=set()
s.add('red')
s.update(['blue','green'])
s2.add('white')
s2.update(['blue','black'])
x=s & s2
x1=s | s2 
print(x,x1)
x2=s - s2 
print(x2)