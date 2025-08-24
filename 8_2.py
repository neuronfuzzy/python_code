def outer():
    data = 0
    def inner():
        nonlocal data
        data += 1
        print(f'data: {data}')
    return inner

my_closure = outer()
my_closure()   # data: 1
my_closure()   # data: 2
my_closure()   # data: 3
