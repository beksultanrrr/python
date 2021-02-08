import operator
d = {2:3}
d.update({1:2})
sorted_d = sorted(d.items(), key=operator.itemgetter(1))
print(sorted_d)