def fib(n):
    counter = 0
    a, b = 0, 1
    print(a, b, end=' ')
    while counter < n - 1:
        print(a + b, end=' ')
        t = a + b
        a = b
        b = t
        counter += 1


def fib_recursive_helper(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fib_recursive_helper(n - 2) + fib_recursive_helper(n - 1)
        return result


def fib_recursive(n):
    if n > 0:
        fib_recursive(n - 1)
    print(fib_recursive_helper(n), end=' ')


fib_recursive(10)
print()
fib(10)
