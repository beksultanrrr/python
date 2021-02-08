d1={'1':10,"2":4}
d2={'2':24,'5':13}
d3={}
for i in (d1,d2):
    d3.update(i)
print(d3)