def f(**kwargs):
    for key in kwargs:
        print(key,kwargs[key])
a={
    '1':2,
    '10':30,
    '20':100
}
user= {
    'fname':'abc',
    'lname':'bbb'
}
f(**a)
f(**user)