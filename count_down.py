import math

def recursive_russian(x, y, z):
    if y <= 0:
        return z

    if y % 2 == 1:
        z = z + x

    return recursive_russian(x + x, y / 2, z)

def recursive_russian(x, y):
    if y == 0:
        return 0
    if y % 2 == 0:
        return 2 * recursive_russian(y / 2, x)
    return x + recursive_russian((y - 1) / 2, x)  

def naive(x, y):
    z = 0
    while y > 0:
        z = z + x
        y = y - 1

    return z

print 0 / 10