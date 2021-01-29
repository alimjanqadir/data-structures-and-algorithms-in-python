def fib(n):
    counter = 0
    a, b = 0, 1
    print(a, b, end=' ')
    while counter < n:
        print(a + b, end=' ')
        t = a + b
        a = b
        b = t
        counter += 1


fib(10)
