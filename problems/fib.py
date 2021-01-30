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


def fib_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fib_recursive(n - 2) + fib_recursive(n - 1)
        return result


