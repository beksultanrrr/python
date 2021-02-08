my_dict = {'1':['a','b'], '2':['c','d']}

my_list = list(my_dict.values())
print(my_list)
for i in my_list[0]:
    for j in range(1, len(my_list)):
        for x in my_list[j]:
            my_string = i + x
            print(my_string)