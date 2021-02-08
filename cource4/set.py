t=[]
l=[1,5,6]
s1=set(l)

s=set(t)
s.add(t)
s.clear()
s.remove()#если надо удалить один элемент
s.pop()#удаляет и возращает какой элемент был удален
x=s.intersection(s1)#пересчение выводит
x=s1.issubset(s) 